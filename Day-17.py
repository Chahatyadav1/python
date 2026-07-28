import boto3

client = boto3.client('ec2')
# response = client.run_instances(
#     BlockDeviceMappings=[
#         {
#             'DeviceName': '/dev/sdh',
#             'Ebs': {
#                 'VolumeSize': 100,
#             },
#         },
#     ],
#     ImageId='ami-00d2dbb426772b03a',
#     InstanceType='t3.micro',
#     KeyName='finac',
#     MaxCount=1,
#     MinCount=1,
#     SecurityGroupIds=[
#         'sg-0c85e00ff3d8848d0',
#     ],
#     SubnetId='subnet-0c637e550d298242c',
#     TagSpecifications=[
#         {
#             'ResourceType': 'instance',
#             'Tags': [
#                 {
#                     'Key': 'Purpose',
#                     'Value': 'test',
#                 },
#             ],
#         },
#     ],
# )
# instance_id = response["Instances"][0]["InstanceId"]
# print(response)
# waiter = client.get_waiter("instance_running")
# waiter.wait(InstanceIds=[instance_id])
# print("sucessfully done")
# response = client.describe_instances(
#     InstanceIds=[
#         'i-0f68a0e0165eff482',
#     ],
# )

response = client.terminate_instances(
    InstanceIds=[
        'i-005c0f4ad53b2e5a2',
    ],
    Force=True,
    SkipOsShutdown=False,
)
instance_id = response["TerminatingInstances"][0]["InstanceId"]
print(response)
waiter=client.get_waiter("instance_terminated")
waiter.wait(InstanceIds=[instance_id])
print("deleted sucessfully")