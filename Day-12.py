from kubernetes import client, config, watch
import subprocess
# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
count = 10
w = watch.Watch()
for ns_ob in w.stream(v1.list_namespace, _request_timeout=60):
    ns=ns_ob['object'].metadata.name
    if ns not in ["kube-system"]:
        try:
            v1.read_namespaced_config_map("company-config",ns)
        except client.exceptions.ApiException as e:
            if e.status == 404:
                ob=subprocess.run(["kubectl","create","configmap","company-config","--from-literal=ENV=production","--from-literal=OWNER=platform-team",f"-n{ns}"],capture_output=True,text=True)
                if ob.returncode == 0:
                    print("sucessfully add cm")
    count -= 1
    if not count:
        w.stop()

print("Ended.")