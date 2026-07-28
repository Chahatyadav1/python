import boto3

client = boto3.client('ec2')
response = client.run_instances(
    BlockDeviceMappings=[
        {
            'Ebs': {
                'DeleteOnTermination': True|False,
                'Iops': 123,
                'SnapshotId': 'string',
                'VolumeSize': 123,
                'VolumeType': 'standard'|'io1'|'io2'|'gp2'|'sc1'|'st1'|'gp3',
                'KmsKeyId': 'string',
                'Throughput': 123,
                'OutpostArn': 'string',
                'AvailabilityZone': 'string',
                'Encrypted': True|False,
                'VolumeInitializationRate': 123,
                'AvailabilityZoneId': 'string',
                'EbsCardIndex': 123
            },
            'NoDevice': 'string',
            'DeviceName': 'string',
            'VirtualName': 'string'
        },
    ],
    ImageId='string',
    InstanceType='t3.micro'
    Ipv6Addresses=[
        {
            'Ipv6Address': 'string',
            'IsPrimaryIpv6': True|False
        },
    ],
    KernelId='string',
    KeyName='string',
    MaxCount=123,
    MinCount=123,
    Monitoring={
        'Enabled': True|False
    },
    Placement={
        'AvailabilityZoneId': 'string',
        'Affinity': 'string',
        'GroupName': 'string',
        'PartitionNumber': 123,
        'HostId': 'string',
        'Tenancy': 'default'|'dedicated'|'host',
        'SpreadDomain': 'string',
        'HostResourceGroupArn': 'string',
        'GroupId': 'string',
        'AvailabilityZone': 'string'
    },
    RamdiskId='string',
    SecurityGroupIds=[
        'string',
    ],
    SecurityGroups=[
        'string',
    ],
    SubnetId='string',
    UserData='string',
    ElasticGpuSpecification=[
        {
            'Type': 'string'
        },
    ],
    ElasticInferenceAccelerators=[
        {
            'Type': 'string',
            'Count': 123
        },
    ],
    TagSpecifications=[
        {
            'ResourceType': 'capacity-reservation'|'client-vpn-endpoint'|'customer-gateway'|'carrier-gateway'|'coip-pool'|'declarative-policies-report'|'dedicated-host'|'dhcp-options'|'egress-only-internet-gateway'|'elastic-ip'|'elastic-gpu'|'export-image-task'|'export-instance-task'|'fleet'|'fpga-image'|'host-reservation'|'image'|'image-usage-report'|'import-image-task'|'import-snapshot-task'|'instance'|'instance-event-window'|'internet-gateway'|'ipam'|'ipam-pool'|'ipam-scope'|'ipv4pool-ec2'|'ipv6pool-ec2'|'key-pair'|'launch-template'|'local-gateway'|'local-gateway-route-table'|'local-gateway-virtual-interface'|'local-gateway-virtual-interface-group'|'local-gateway-route-table-vpc-association'|'local-gateway-route-table-virtual-interface-group-association'|'natgateway'|'network-acl'|'network-interface'|'network-insights-analysis'|'network-insights-path'|'network-insights-access-scope'|'network-insights-access-scope-analysis'|'outpost-lag'|'placement-group'|'prefix-list'|'replace-root-volume-task'|'reserved-instances'|'route-table'|'security-group'|'security-group-rule'|'service-link-virtual-interface'|'snapshot'|'spot-fleet-request'|'spot-instances-request'|'subnet'|'subnet-cidr-reservation'|'traffic-mirror-filter'|'traffic-mirror-session'|'traffic-mirror-target'|'transit-gateway'|'transit-gateway-attachment'|'transit-gateway-connect-peer'|'transit-gateway-multicast-domain'|'transit-gateway-policy-table'|'transit-gateway-metering-policy'|'transit-gateway-route-table'|'transit-gateway-route-table-announcement'|'volume'|'vpc'|'vpc-endpoint'|'vpc-endpoint-connection'|'vpc-endpoint-service'|'vpc-endpoint-service-permission'|'vpc-peering-connection'|'vpn-connection'|'vpn-gateway'|'vpc-flow-log'|'capacity-reservation-fleet'|'traffic-mirror-filter-rule'|'vpc-endpoint-connection-device-type'|'verified-access-instance'|'verified-access-group'|'verified-access-endpoint'|'verified-access-policy'|'verified-access-trust-provider'|'vpn-connection-device-type'|'vpc-block-public-access-exclusion'|'vpc-encryption-control'|'route-server'|'route-server-endpoint'|'route-server-peer'|'ipam-resource-discovery'|'ipam-resource-discovery-association'|'instance-connect-endpoint'|'verified-access-endpoint-target'|'ipam-external-resource-verification-token'|'capacity-block'|'mac-modification-task'|'ipam-prefix-list-resolver'|'ipam-policy'|'ipam-prefix-list-resolver-target'|'secondary-interface'|'secondary-network'|'secondary-subnet'|'capacity-manager-data-export'|'vpn-concentrator'|'ipam-pool-allocation'|'capacity-reservation-cancellation-quote',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
)