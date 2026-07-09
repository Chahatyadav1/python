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

#---------testing service connectivity-----


# import yaml
# import time
# from kubernetes import client, config
# import subprocess
# config.load_kube_config()
# v1 = client.CoreV1Api()
# with open("pod.yaml","r") as f:
#     b=yaml.safe_load(f)
# res=v1.create_namespaced_pod(namespace="default", body=b)
# print(f"Pod created. '{res.metadata.name}'")
# while True:
#     pod = v1.read_namespaced_pod(
#         name=res.metadata.name,
#         namespace="default"
#     )

#     if pod.status.phase == "Running":
#         print("Pod is Running")
#         break

#     print("Waiting for pod...")
#     time.sleep(2)
# svc=v1.list_service_for_all_namespaces()
# for i in svc.items:
#     if i.spec.type == "ClusterIP":
#         name=i.metadata.name
#         ip=i.spec.cluster_ip
#         port=i.spec.ports[0].port
#         out=subprocess.run(["kubectl","exec",res.metadata.name,"--","curl","--fail",f"http://{ip}:{port}"],text=True,capture_output=True)
#         print("--"*40)
#         if out.returncode == 0:
#             print(f"Name: {name:<20}\t Status: PASS")
#         else:
#             print(f"Name: {name:<20}\t Status: Fail")
# v1.delete_namespaced_pod(
#     name=res.metadata.name,
#     namespace="default"
# )

# from kubernetes import client, config
# import time
# config.load_kube_config()
# v1 = client.AppsV1Api()
# resp=v1.list_deployment_for_all_namespaces()
# for i in resp.items:
#     name=i.metadata.name
#     namespace=i.metadata.namespace
#     while True:
#         j=v1.read_namespaced_deployment(name=name,namespace=namespace)       
#         if j.spec.replicas == j.status.ready_replicas:
#             print(f"Watching deployment: {name}")
#             print("--"*40)
#             print(f"Desired Replicas: {j.spec.replicas:<20}")
#             print(f"Updated Replicas: {j.status.updated_replicas:<20}")
#             print(f"Avilable: {j.status.available_replicas:<20}")
#             print(f"Ready: {j.status.ready_replicas:<20}")
#             print("Rollout completed successfully.")
#             break
#         else:
#             print(f"Watching deployment: {name}")
#             print("--"*40)
#             print(f"Desired Replicas: {j.spec.replicas:<20}")
#             print(f"Updated Replicas: {j.status.updated_replicas:<20}")
#             print(f"Avilable: {j.status.available_replicas:<20}")
#             print(f"Ready: {j.status.ready_replicas:<20}")
#             print("Waiting...")
#             time.sleep(2)


# from kubernetes import client, config, watch

# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()

# v1 = client.AppsV1Api()
# count = 10
# w = watch.Watch()
# for event in w.stream(v1.list_deployment_for_all_namespaces, _request_timeout=60):

#     print("Event: %s %s" % (event['type'], event['object'].metadata.name))
#     count -= 1
#     if not count:
#         w.stop()

# print("Ended.")

# from kubernetes import client, config, watch

# config.load_kube_config()

# v1 = client.CoreV1Api()
# w = watch.Watch()
# count=12
# for event in w.stream(v1.list_pod_for_all_namespaces):
#     pod = event["object"]

#     print(
#         event["type"],
#         pod.metadata.namespace,
#         pod.metadata.name,
#         pod.status.phase
#     )
#     if event["type"] == "ADDED":
#         count-=1
#     if count == 0:
#         break

# from kubernetes import client, config, watch

# config.load_kube_config()

# v1 = client.CoreV1Api()
# w = watch.Watch()
# count=12
# for event in w.stream(v1.list_namespaced_pod(namespace="default")):
#     print(event)


# from kubernetes import client, config, watch

# config.load_kube_config()

# apps = client.AppsV1Api()
# w = watch.Watch()

# print("Watching Deployments...\n")

# for event in w.stream(apps.list_deployment_for_all_namespaces):
#     deploy = event["object"]

#     print("=" * 60)
#     print(f"Event:               {event['type']}")
#     print(f"Namespace:           {deploy.metadata.namespace}")
#     print(f"Deployment:          {deploy.metadata.name}")
#     print(f"Desired Replicas:    {deploy.spec.replicas}")
#     print(f"Updated Replicas:    {deploy.status.updated_replicas}")
#     print(f"Available Replicas:  {deploy.status.available_replicas}")
#     print(f"Ready Replicas:      {deploy.status.ready_replicas}")

#     desired = deploy.spec.replicas or 0
#     ready = deploy.status.ready_replicas or 0

#     if desired == ready:
#         print("Status: Rollout completed successfully.")
#     else:
#         print("Status: Rollout in progress...")

