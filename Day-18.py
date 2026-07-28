import boto3

client = boto3.client('ec2')
response = client.create_vpc(
    CidrBlock='10.0.0.0/16',
)
vpc_id=response["Vpc"]["VpcId"]
print("Wait for vpc to be created...")
waiter=client.get_waiter("vpc_available")
waiter.wait(VpcIds=[vpc_id])
print("vpc sucessfully created")
response1 = client.modify_vpc_attribute(
    EnableDnsHostnames={
        'Value': True
    },
    EnableDnsSupport={
        'Value': True
    },
    VpcId=vpc_id,
)
print(f"Vpc Id: {vpc_id}")
print("wait for vpc to enable Dns Hostnames and Dns support...")
waiter=client.get_waiter("vpc_available")
waiter.wait(VpcIds=[vpc_id])
print("vpc sucessfully updated ")
#-----create public subnet--------
response2 = client.create_subnet(
    CidrBlock='10.0.1.0/24',
    VpcId=vpc_id,
)
subnet_id=response2["Subnet"]["SubnetId"]
print("wait for subnet to be created.....")
waiter=client.get_waiter("subnet_available")
waiter.wait(SubnetIds=[subnet_id])
print("subnet sucessfully created")
print(f"Subnet Id: {subnet_id}")

response3 = client.create_internet_gateway(
)
igw_id=response3["InternetGateway"]["InternetGatewayId"]
print(f"igw-id: {igw_id}")
response = client.attach_internet_gateway(
    DryRun=False,
    InternetGatewayId=igw_id,
    VpcId=vpc_id
)