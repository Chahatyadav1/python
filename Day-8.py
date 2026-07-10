import yaml

with open("pod.yaml") as f:
    data=f.read()
    y=yaml.safe_load(data)
try:
    if y["kind"] == "Pod":
        containers=y["spec"]["containers"]
        for container in containers:
            
            image = container["image"]
            if image is None:
                print("validation failed image field is empty")
            else:
                print("image validation sucess")
                resources = container.get("resources", {})
                limits = resources.get("limits", {})
                requests = resources.get("requests", {})

                limit_cpu = limits.get("cpu")
                limit_memory = limits.get("memory")
                request_cpu = requests.get("cpu")
                request_memory = requests.get("memory")
                if  limit_cpu is None or  limit_memory is None or  request_cpu is None or  request_memory is None:
                    print("validation failed for resource filed is empty")
                else:
                    print("validation pass")
    elif y["kind"] == "Deployment":
        pass
    elif y["kind"] == "Service":
        pass
    else:
        print("this kind of object is not yet configured to validate")
except KeyError as e:
      print(f"resource filed not exist {e}")