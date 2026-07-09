from kubernetes import client, config, watch
config.load_kube_config()
v1 = client.CoreV1Api()
