from kubernetes import client, config, watch
import subprocess
import logging
from flask import Flask
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s')
config.load_incluster_config()
app=Flask(__name__)
v1 = client.CoreV1Api()
count = 10
w = watch.Watch()
for event in w.stream(v1.list_pod_for_all_namespaces, _request_timeout=60):
    print("Event: " , event['type'], event['object'].metadata.name)
    labels = event['object'].metadata.labels or {}
    if "run" not in labels:
        ob=subprocess.run(["kubectl","patch","pod",event['object'].metadata.name,"-p",'{"metadata":{"labels":{"run":"tested"}}}',f"-n{event['object'].metadata.namespace}",],capture_output=True,text=True)
        if ob.returncode == 0:
            logger.info("Pached sucessfully")
        else:
            print(ob.stderr)
    count -= 1
    if not count:
        w.stop()
print("Ended.")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)