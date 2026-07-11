# import yaml

# with open("pod.yaml") as f:
#     data=f.read()
#     y=yaml.safe_load(data)
# try:
#     if y["kind"] == "Pod":
#         containers=y["spec"]["containers"]
#         for container in containers:
            
#             image = container["image"]
#             if image is None:
#                 print("validation failed image field is empty")
#             else:
#                 print("image validation sucess")
#                 resources = container.get("resources", {})
#                 limits = resources.get("limits", {})
#                 requests = resources.get("requests", {})

#                 limit_cpu = limits.get("cpu")
#                 limit_memory = limits.get("memory")
#                 request_cpu = requests.get("cpu")
#                 request_memory = requests.get("memory")
#                 if  limit_cpu is None or  limit_memory is None or  request_cpu is None or  request_memory is None:
#                     print("validation failed for resource filed is empty")
#                 else:
#                     print("validation pass")
#     elif y["kind"] == "Deployment":
#         pass
#     elif y["kind"] == "Service":
#         pass
#     else:
#         print("this kind of object is not yet configured to validate")
# except KeyError as e:
#       print(f"resource filed not exist {e}")

# import subprocess
# import re
# pattern = (
#     r"(?P<id>\S+)\s+"
#     r"(?P<image>\S+)\s+"
#     r'(?P<command>".*?")\s+'
#     r"(?P<created>\d+\s+\w+\s+ago)\s+"
#     r"(?P<status>Exited\s+\(\d+\)\s+\d+\s+\w+\s+ago)\s+"
#     r"(?P<name>\S+)$"
# )
# img_pattern=(
#     r"(?P<repo>\S+)\s+"
#     r"(?P<tag>\S+)\s+"
#     r"(?P<image>\S+)\s+"
#     r"(?P<created>\d+\s+\S+\s+ago)\s+"
#     r"(?P<size>\d+\.\d+).*"
# )
# o=subprocess.run(["docker","images","-f","dangling=true"],capture_output=True,text=True)
# dang=o.stdout
# da=dang.splitlines()
# for i in da[1:]:
#     f=re.search(img_pattern,i)
#     print(f.group("image"))
#     del1=subprocess.run(["docker","rmi",f.group("image")])
#     if del1.returncode == 0:
#         print("dangling image delete sucessfully")
#     else:
#         print(f"Error in deleting image:{del1.stderr}")
# ob=subprocess.run(["docker","ps","-a"],capture_output=True,text=True)
# data=ob.stdout.splitlines()
# for i in data[1:]:
#     d=re.search(pattern,i)
#     status=d.group("status")
#     if status.startswith("Exited") :
#         print(f"container deleteing! :{d.group('name')}")
#         a=subprocess.run(["docker","rm",d.group("id")],capture_output=True)
#         if a.returncode == 0:
#             print("container delete sucessfully")
#         else:
#             print(f"Fatal error:{a.stderr}")

import yaml

with open("pod.yaml") as o:
    old=yaml.safe_load(o)
with open("pod1.yaml") as n:
    new=yaml.safe_load(n)
for data in old:
    if old[data] != new[data]:
        print(f"{old[data]} -> {new[data]}")