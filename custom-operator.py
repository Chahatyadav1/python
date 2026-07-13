from kubernetes import client,config,watch
import logging
from kubernetes.client.rest import ApiException

config.load_kube_config()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s')
api = client.CustomObjectsApi()
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
    port=obj["spec"].get("port")
    image=obj["spec"].get("image")
    apps_v1=client.AppsV1Api()
    try:
        deploy=apps_v1.read_namespaced_deployment(name=name,namespace=namespace)
        logger.info("deployment exist")
        if last_replicas is None:
            last_replicas = replicas
            continue
        if last_port is None:
            last_port = port
            continue
        if last_image is None:
            last_image = image
            continue

        if replicas != last_replicas:
            body={
                "spec": {
                    "replicas": replicas
                }
            }
            resp=apps_v1.patch_namespaced_deployment(name=name,namespace=namespace,body=body)
            logger.info(f"deployment: {resp.metadata.name} is sucessfullt scaled from {last_replicas} -> {replicas}")
    except ApiException as e:
        if e.status == 404:
            payload={
                "apiVerson": "apps/v1",
                "kind": "Deployment",
                "metadata": {
                    "name": name ,
                    "namespace": namespace,
                },
                "spec": {
                    "replicas": replicas,
                    "selector": {
                        "matchLabels": {
                            "app": "nginx"
                        }
                    },
                    "template": {
                        "metadata": {
                            "labels": {
                                "app": "nginx"
                            }
                        },
                        "spec": {
                            "containers": [
                                {
                                    "name": "nginx",
                                    "image": image,
                                    "ports": [
                                        {
                                            "containerPort": 80
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
            }
            re=apps_v1.create_namespaced_deployment(name=name,namespace=namespace,body=payload)
            logger.info(f"deploy created :{re.metadata.name} in namespace :{re.metadata.namespace}")
        else:
            logger.critical("something wrong cr not present")
        