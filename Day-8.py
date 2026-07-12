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

# import yaml

# def compare(old,new,path=""):
#     if isinstance(old, dict) and isinstance(new,dict):
#         keys = set(old.keys()) | set(new.keys()) 
#         for key in keys:
#             new_path=f"{path}.{key}" if path else key
#             if key not in old:
#                 print(f"{new_path} added")
#                 print(new[key])
#                 continue
#             if key not in new:
#                 print(f"{new_path}: removed")
#                 print(old[key])
#                 continue
#             compare(old[key],new[key])
#     elif isinstance(old, list) and isinstance(new, list):
#         max_len = max(len(old), len(new))
#         for i in range(max_len):
#             new_path = f"{path}[{i}]"
#             if i >= len(old):
#                 print(f"{new_path} added:")
#                 print(f"  {new[i]}")
#                 continue

#             if i >= len(new):
#                 print(f"{new_path} removed:")
#                 print(f"  {old[i]}")
#                 continue
#             compare(old[i], new[i], new_path)
#     else:
#         if old != new:
#             print(f"{path} changed:")
#             print(f"  {old} -> {new}")
# with open("pod.yaml") as o:
#     old=yaml.safe_load(o)
# with open("pod1.yaml") as n:
#     new=yaml.safe_load(n)
# compare(old,new)

# import requests

# a=requests.get("https://jsonplaceholder.typicode.com")
# if a.status_code == 200 :
#     print("sucess")
#     print(a)
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)
# print(r.text)
# r = requests.get('https://api.github.com/events')
# print(r.json())
# r = requests.post('https://httpbin.org/post', data=payload)
# print(r.headers)

# import requests
# import os
# token = os.getenv("GITHUB_TOKEN")
# headers = {
#     "Authorization": f"Bearer {token}",
#     "Accept": "application/vnd.github+json",
# }
# response=requests.get("https://api.github.com/rate_limit")
# print(response.json())
