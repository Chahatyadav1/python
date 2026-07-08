from kubernetes import client, config
config.load_kube_config()
v1 = client.CoreV1Api()
ret=v1.list_node(watch=False)
for i in ret.items:
    print("-"*40)
    print(f"Node: {i.metadata.name:<20}")
    for condition in i.status.conditions:
        if condition.type == "Ready":
            if condition.status == "True":
                print("Ready")
            else:
                print("Not Ready")
    
    print("\n\n")
    print(f"CPU Capacity: {i.status.capacity["cpu"]:<20}")
    print(f"Memory capacity: {i.status.capacity["memory"]:<20}")
    print("\n\n")
    print(f"CPU Allocable: {i.status.allocatable["cpu"]:<20}")
    print(f"Memory Allocation: {i.status.allocatable["memory"]:<20}")
    print("\n\n")
    print(f"Pod capacity: {i.status.capacity["pods"]:<20}")
    print(f"Memory Allocation: {i.status.allocatable["pods"]:<20}")
    print("\n\n")
    print(f"OS Image: {i.status.node_info.os_image:<20}") 
    print(f"Kernel Version: {i.status.node_info.kernel_version:<20}") 
    print(f"Container Runtime: {i.status.node_info.container_runtime_version:<20}") 
    print(f"Kubelet Version: {i.status.node_info.kubelet_version:<20}")   
    print(f"Kubelet Version: {i.status.node_info.architecture:<20}")  
    print("-"*40)
