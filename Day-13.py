from kubernetes import client, config, watch
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s')
try:
    config.load_kube_config()
    logger.info("configured locally")

except:
    config.incluster_config()
    logger.info("configured inside container")
v1 = client.AppsV1Api()

w = watch.Watch()
for event in w.stream(v1.list_deployment_for_all_namespaces, _request_timeout=60):
    lb = event["object"].metadata.labels or {}
    containers = event["object"].spec.template.spec.containers
    if lb.get("inject-sidecar") == "true" and not any (c.name == "logger" for c in containers):
        body={
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {
                             "name": "logger",
                             "image": "busybox",
                             "command": ["sh","-c","sleep 1d"]
                            }
                        ]
                    }
                }
            }
        }
        resp = v1.patch_namespaced_deployment(event["object"].metadata.name,event["object"].metadata.namespace,body)
        print(f"container pached. Status='{resp.spec.template.spec.containers[0].name}'")
        logger.info("container sucessfully pached")

print("Ended.")