# from kubernetes import client, config, watch
# import subprocess
# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()

# v1 = client.CoreV1Api()
# count = 10
# w = watch.Watch()
# for ns_ob in w.stream(v1.list_namespace, _request_timeout=60):
#     ns=ns_ob['object'].metadata.name
#     if ns not in ["kube-system"]:
#         try:
#             v1.read_namespaced_config_map("company-config",ns)
#         except client.exceptions.ApiException as e:
#             if e.status == 404:
#                 ob=subprocess.run(["kubectl","create","configmap","company-config","--from-literal=ENV=production","--from-literal=OWNER=platform-team",f"-n{ns}"],capture_output=True,text=True)
#                 if ob.returncode == 0:
#                     print("sucessfully add cm")
#     count -= 1
#     if not count:
#         w.stop()

# print("Ended.")

from kubernetes import client, config, watch
from flask import Flask
import logging
app=Flask(__name__)
@app.route("/healthz")
def healthz():
    return {"ok": "200"}
@app.route("/")
def controller():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s')
    try:
        config.load_incluster_config()
        logger.info("Using in-cluster configuration")
    except config.ConfigException:
        config.load_kube_config()
        logger.info("Using local kubeconfig")
    v1 = client.CoreV1Api()
    w = watch.Watch()
    for ns_ob in w.stream(v1.list_namespace, _request_timeout=60):
        ns=ns_ob['object'].metadata.name
        if ns not in ["kube-system","local-path-storage","kube-node-lease","kube-public"]:
            try:
                v1.read_namespaced_config_map("company-config",ns)
            except client.exceptions.ApiException as e:
                if e.status == 404:
                    body = client.V1ConfigMap(
                        metadata=client.V1ObjectMeta(
                            name="company-config"
                        ),
                        data={
                            "ENV": "production",
                            "OWNER": "platform-team"
                        }
                    )
                    resp=v1.create_namespaced_config_map(namespace=ns,body=body)
                    logger.info("Created ConfigMap '%s' in namespace '%s'",resp.metadata.name, ns)
                else:
                    logger.error("API error: %s", e)
controller()
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)