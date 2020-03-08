import boto3 

region  = "ap-south-1"
project = ('tag:Project','geo')
dev     = ('tag:Env','dev')
test    = ('tag:Env','test')

def status(region,project,env):
    client = boto3.client('ec2', region_name=region)

    response = client.describe_instances(
        Filters=[
            {'Name':project[0], 'Values':[project[1]]},
            {'Name':env[0], 'Values':[env[1]]}     
        ]
    )

    for reservations in response['Reservations']:
        for instances in reservations['Instances']:
            if instances['State']['Code'] == 16:
                # client.stop_instances(
                #     InstanceIds = [instances['InstanceId']]
                # )
                print ("running")
            elif instances['State']['Code'] == 80:
                # client.start_instances(
                #     InstanceIds = [instances['InstanceId']]
                # )
                print ("stopped")

status(region,project,dev)
status(region,project,test)