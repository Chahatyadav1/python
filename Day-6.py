# from kubernetes import client, config
# config.load_kube_config()
# v1 = client.CoreV1Api()
# ret=v1.list_node(watch=False)
# for i in ret.items:
#     print("-"*40)
#     print(f"Node: {i.metadata.name:<20}")
#     for condition in i.status.conditions:
#         if condition.type == "Ready":
#             if condition.status == "True":
#                 print("Ready")
#             else:
#                 print("Not Ready")
    
#     print("\n\n")
#     print(f"CPU Capacity: {i.status.capacity["cpu"]:<20}")
#     print(f"Memory capacity: {i.status.capacity["memory"]:<20}")
#     print("\n\n")
#     print(f"CPU Allocable: {i.status.allocatable["cpu"]:<20}")
#     print(f"Memory Allocation: {i.status.allocatable["memory"]:<20}")
#     print("\n\n")
#     print(f"Pod capacity: {i.status.capacity["pods"]:<20}")
#     print(f"Memory Allocation: {i.status.allocatable["pods"]:<20}")
#     print("\n\n")
#     print(f"OS Image: {i.status.node_info.os_image:<20}") 
#     print(f"Kernel Version: {i.status.node_info.kernel_version:<20}") 
#     print(f"Container Runtime: {i.status.node_info.container_runtime_version:<20}") 
#     print(f"Kubelet Version: {i.status.node_info.kubelet_version:<20}")   
#     print(f"Kubelet Version: {i.status.node_info.architecture:<20}")  
#     print("-"*40)

import yaml
import time
from kubernetes import client, config
import subprocess
config.load_kube_config()
v1 = client.CoreV1Api()
with open("pod.yaml","r") as f:
    b=yaml.safe_load(f)
res=v1.create_namespaced_pod(namespace="default", body=b)
print(f"Pod created. '{res.metadata.name}'")
while True:
    pod = v1.read_namespaced_pod(
        name=res.metadata.name,
        namespace="default"
    )

    if pod.status.phase == "Running":
        print("Pod is Running")
        break

    print("Waiting for pod...")
    time.sleep(2)
svc=v1.list_service_for_all_namespaces()
for i in svc.items:
    if i.spec.type == "ClusterIP":
        name=i.metadata.name
        ip=i.spec.cluster_ip
        port=i.spec.ports[0].port
        out=subprocess.run(["kubectl","exec",res.metadata.name,"--","curl","--fail",f"http://{ip}:{port}"],text=True,capture_output=True)
        print("--"*40)
        if out.returncode == 0:
            print(f"Name: {name:<20}\t Status: PASS")
        else:
            print(f"Name: {name:<20}\t Status: Fail")
v1.delete_namespaced_pod(
    name=res.metadata.name,
    namespace="default"
)

