import boto3
import json
client = boto3.client('ec2')
response = client.describe_instances()
print(response)
print(json.dumps(response, default=str, indent=4))
print(response["Reservations"][0]["Instances"][0]["VpcId"])