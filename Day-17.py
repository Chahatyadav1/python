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

print(response)