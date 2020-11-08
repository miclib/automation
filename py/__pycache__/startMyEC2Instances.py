import sys 
import boto3

from botocore.exceptions import ClientError



ec2 = boto3.client('ec2',region_name='eu-west-2')

isId='i-06dcd0cf1b5d639c5'

try: 
        response = ec2.start_instances(InstanceIds=[isId],DryRun=False)
        print(response)

except ClientError as e:
        print(e)
    
