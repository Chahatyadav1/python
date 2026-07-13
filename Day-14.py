# image policy controller

# from kubernetes import client, config, watch
# import logging

# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s')
# try:
#     config.load_kube_config()
#     logger.info("configured locally")

# except:
#     config.incluster_config()
#     logger.info("configured inside container")
# v1 = client.AppsV1Api()

# w = watch.Watch()
# for event in w.stream(v1.list_deployment_for_all_namespaces, _request_timeout=60):
#     name=event["object"].metadata.name
#     namespace=event["object"].metadata.namespace
#     containers = event["object"].spec.template.spec.containers
#     if namespace in ["default"] and any (not  (c.image.startswith("docker.io/chahatyadav1/") ) for c in containers):
#         data={
#             "spec": {
#                 "replicas" : 0
#             }
#         }
#         resp=v1.patch_namespaced_deployment(name,namespace,data)
#         if event["object"].spec.replicas == 0:
#             logger.info(f"deployment :{name} scales to 0 Due to Image policy violated")
#         else:
#             logger.info("some error found")


# add resource quatas when crate a new ns?

from kubernetes import client,config,watch
from kubernetes.client.rest import ApiException

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s')
try:
    config.load_kube_config()
    logger.info("configured locally")
except:
    config.load_incluster_config()
    logger.info("configured inside pod/deploy")

v1= client.CoreV1Api()
w = watch.Watch()

for event in w.stream(v1.list_namespace, _request_timeout=60):
    namespace=event["object"].metadata.name
    try:
        v1.read_namespaced_resource_quota("compute-quota", namespace)
        quota_exists = True
    except ApiException as e:
        if e.status == 404:
            quota_exists = False
        else:
            logger.critical(e)
    if event["type"] == "ADDED" and quota_exists == False:
        quota = client.V1ResourceQuota(
            metadata=client.V1ObjectMeta(name="compute-quota",namespace=namespace),
            spec=client.V1ResourceQuotaSpec(
                hard={
                    "limits.cpu": "4",
                    "limits.memory": "8Gi",
                    "pods": "20"
                }
            )
        )
        resp=v1.create_namespaced_resource_quota(namespace=namespace,body=quota)
        logger.info(f"quata sucessfilly creatde :{resp.metadata.name} in namespace :{resp.metadata.namespace}")