from kubernetes import client, config, watch
import logging
from kubernetes.client.rest import ApiException

config.load_kube_config()

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
)

api = client.CustomObjectsApi()
v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()
w = watch.Watch()

group = "stable.com"
version = "v1"
plural = "demos"
namespace = "default"
name = "demo-cr"

last_replicas = None
last_port = None
last_image = None

for event in w.stream(
    api.list_namespaced_custom_object,
    group=group,
    version=version,
    namespace=namespace,
    plural=plural,
):
    obj = event["object"]

    if obj["metadata"]["name"] != name:
        continue

    replicas = obj["spec"].get("replicas")
    port = obj["spec"].get("port")
    image = obj["spec"].get("image")

    # --- Deployment reconciliation ---
    try:
        deploy = apps_v1.read_namespaced_deployment(name=name, namespace=namespace)
        logger.info("deployment exists")

        if last_replicas is None:
            # first time we've seen it - just sync our tracked state, don't patch
            last_replicas = replicas
            last_port = port
            last_image = image
        else:
            patch_spec = {}
            container_patch = {}

            if replicas != last_replicas:
                patch_spec["replicas"] = replicas
            if image != last_image:
                container_patch["image"] = image
            if port != last_port:
                container_patch["ports"] = [{"containerPort": port}]

            if container_patch:
                container_patch["name"] = "nginx"
                patch_spec["template"] = {
                    "spec": {"containers": [container_patch]}
                }

            if patch_spec:
                body = {"spec": patch_spec}
                resp = apps_v1.patch_namespaced_deployment(
                    name=name, namespace=namespace, body=body
                )
                logger.info(
                    f"deployment {resp.metadata.name} updated "
                    f"(replicas {last_replicas}->{replicas}, "
                    f"image {last_image}->{image}, containerPort {last_port}->{port})"
                )
                last_replicas = replicas
                last_image = image
    except ApiException as e:
        if e.status == 404:
            payload = {
                "apiVersion": "apps/v1",
                "kind": "Deployment",
                "metadata": {
                    "name": name,
                    "namespace": namespace,
                },
                "spec": {
                    "replicas": replicas,
                    "selector": {
                        "matchLabels": {"app": "nginx"}
                    },
                    "template": {
                        "metadata": {
                            "labels": {"app": "nginx"}
                        },
                        "spec": {
                            "containers": [
                                {
                                    "name": "nginx",
                                    "image": image,
                                    "ports": [{"containerPort": port or 80}],
                                }
                            ]
                        },
                    },
                },
            }
            re = apps_v1.create_namespaced_deployment(namespace=namespace, body=payload)
            logger.info(f"deployment created: {re.metadata.name} in namespace {re.metadata.namespace}")
            last_replicas = replicas
            last_image = image
        else:
            logger.critical(f"unexpected error reading deployment: {e}")
            continue

    # --- Service reconciliation ---
    try:
        svc = v1.read_namespaced_service(name=name, namespace=namespace)

        if port != last_port:
            svc_patch = {
                "spec": {
                    "ports": [{"protocol": "TCP", "port": 80, "targetPort": port}]
                }
            }
            v1.patch_namespaced_service(name=name, namespace=namespace, body=svc_patch)
            logger.info(f"service {name} updated targetPort {last_port}->{port}")
            last_port = port

    except ApiException as e:
        if e.status == 404:
            svc_body = {
                "apiVersion": "v1",
                "kind": "Service",
                "metadata": {"name": name},
                "spec": {
                    "selector": {"app": "nginx"},
                    "ports": [
                        {"protocol": "TCP", "port": 80, "targetPort": port}
                    ],
                },
            }
            svc = v1.create_namespaced_service(namespace=namespace, body=svc_body)
            logger.info(f"service created: {svc.metadata.name} in namespace {namespace}")
            last_port = port
        else:
            logger.info(f"service issue: {e}")