# import json
# data={"Name":"Chahat","Age":"2"}
# a=json.dumps(data) # convert dict to str
# b=json.loads(data) # convert str to dict
# print(a)

# import requests

# a=requests.get("http://api.github.com")
# print(a.status_code)
# # print(a.text)
# obj=a.json()
# print(obj["emails_url"])
# data={
#     "test": "data",
#     "daily": "preactice"
# }
# url="https://httpbin.org/post"
# b=requests.post(url,json=data)
# print(b.json())

import yaml
import subprocess
with open("pod.yaml","r") as f:
    print(f)
    lines=yaml.safe_load(f)
print(lines)
data=yaml.dump(lines)
print(data)


output = subprocess.run(
    ["kubectl", "get", "pods"],
    capture_output=True,
    text=True
)