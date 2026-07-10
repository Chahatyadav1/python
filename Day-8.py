import yaml

with open("pod.yaml") as f:
    data=f.read()
    y=yaml.safe_load(data)
print(y[kind])