# info = 0
# warning = 0
# error = 0

# with open("app.log", "r") as f:
#     for line in f:
#         if "INFO" in line:
#             info += 1
#         elif "WARNING" in line:
#             warning += 1
#         elif "ERROR" in line:
#             error += 1

# print(f"INFO: {info}")
# print(f"WARNING: {warning}")
# print(f"ERROR: {error}")


#project -2 


# import psutil

# disk=psutil.disk_usage('/')

# print(f"total:{disk.total}")
# print(f"usage:{disk.used}")
# print(f"free:{disk.free}")
# if(disk.percent > 80.0):
#     print("Alert high usage")

# import psutil
# battery = psutil.sensors_battery()
# print(battery)

# import os
# import shutil
# a=os.listdir(path='.')
# os.mkdir("Demo")
# for i in a:
#     if os.path.isfile(i) and not i.endswith(".log"):
#         shutil.copy(i, "Demo")

# import os
# # print(os.getenv("USER"))
# for key in os.environ:
#     print(f"{key}: {os.environ[key]}")

# import json
# k = "projects"
# with open("sample.json","r") as f:
#     a=json.load(f)
#     print(a)
# for i in a:
#     if k == i:
#         print("key found",i)

# -- intermediate 

# import subprocess
# a=subprocess.run(["kubectl","get","pod","-o","name"],capture_output=True,text=True)
# a1=a.stdout.splitlines()
# b=subprocess.run(["kubectl","get","nodes"])
# for i in a1:
#   d=subprocess.run(["kubectl","describe",i])
# print(d)

# import subprocess
# import sys

# b = subprocess.run(
#     "docker images --filter dangling=true -q",
#     capture_output=True,
#     text=True,
#     shell=True
# )

# imgs = b.stdout.splitlines()

# if not imgs:
#     print("No dangling images found.")
#     sys.exit()

# print("Dangling images:")
# for img in imgs:
#     print(img)

# choice = input("Are you sure you want to delete these images? (y/n): ").lower()

# match choice:
#     case "y":
#         for img in imgs:
#             subprocess.run(["docker", "rmi", img])
#         print("Images deleted.")
#     case "n":
#         print("Operation cancelled.")
#     case _:
#         print("Invalid choice.")


# import subprocess
# import sys

# result = subprocess.run(
#     ["kubectl", "get", "pods", "-A", "--no-headers"],
#     capture_output=True,
#     text=True
# )

# if result.returncode != 0:
#     print("Error:", result.stderr)
#     sys.exit(1)

# running = []
# pending = []
# crashloop = []

# # Convert multiline output into a list of lines
# pods = result.stdout.splitlines()

# for pod in pods:
#     cols = pod.split()

#     namespace = cols[0]
#     pod_name = cols[1]
#     status = cols[3]

#     if status == "Running":
#         running.append((namespace, pod_name))

#     elif status == "Pending":
#         pending.append((namespace, pod_name))

#     elif status == "CrashLoopBackOff":
#         crashloop.append((namespace, pod_name))

# print("=" * 50)
# print("              POD HEALTH REPORT")
# print("=" * 50)

# print(f"\nRunning Pods ({len(running)})")
# print("-" * 50)
# for ns, pod in running:
#     print(f"{ns:<20} {pod}")

# print(f"\nPending Pods ({len(pending)})")
# print("-" * 50)
# for ns, pod in pending:
#     print(f"{ns:<20} {pod}")

# print(f"\nCrashLoopBackOff Pods ({len(crashloop)})")
# print("-" * 50)
# for ns, pod in crashloop:
#     print(f"{ns:<20} {pod}")

# print("\n" + "=" * 50)
# print(f"Total Pods            : {len(pods)}")
# print(f"Running Pods          : {len(running)}")
# print(f"Pending Pods          : {len(pending)}")
# print(f"CrashLoopBackOff Pods : {len(crashloop)}")
# print("=" * 50)

# import yaml
# with open("pod.yaml","r") as f:
#     a=yaml.safe_load(f)
# print(a)
# kind=a["kind"]
# name=a["metadata"]["name"]
# namespace=a["metadata"]["namespace"]
# container_image=a["spec"]["containers"][0]["image"]
# container_ports=a["spec"]["containers"][0]["ports"][0]["containerPort"]
# print(kind)
# print(name)
# print(namespace)
# print(container_image)
# print(container_ports)
# # print(a)

# from kubernetes import client, config


# config.load_kube_config()

# v1 = client.CoreV1Api()
# a=dir(v1)
# help(v1.list_service_for_all_namespaces)
# print("Listing pods with their IPs:")
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in a:
#     print(i)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
# rem = v1.list_service_for_all_namespace(watch=False)
# for i in rem.items:
#     print("%s\t%s" %  (i.metadata.namespace, i.metadata.name))

# from kubernetes import config, client
# # config.load_kube_config()
# v1 = client.CoreV1Api()
# a=dir(v1)
# with open("api.txt","w") as f:
#     for i in a:
#         if not i.startswith("_"):
#             f.write(str(i)+"\n")

from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()
ret = v1.list_namespaced_secret(namespace="default")

name_list = []
namespace_list = []

for i in ret.items:
    name = i.metadata.name
    namespace = i.metadata.namespace

    name_list.append(name)
    namespace_list.append(namespace)

    if not i.data:
        print(f"{namespace}/{name}: No data found")
        continue

    for key, value in i.data.items():
        print(f"Key: {key}")
        print(f"Value (Base64): {value}")