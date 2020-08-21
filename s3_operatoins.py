import logging
import boto3
from botocore.exceptions import ClientError
import pprint

def list_all_regions():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    for item in response['Regions']:
        print(item)

def create_bucket(name, region="eu-central-1"):
    try:
        s3_client = boto3.client('s3')
        location = {'LocationConstraint': region}
        response = s3_client.create_bucket(
            ACL='private',
            Bucket=name,
            CreateBucketConfiguration= location,
        )
        logging.info("bucket created")
        logging.info(response)

    except ClientError as e:
        logging.error(e)

def list_buckets():
    try:
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        logging.info("buckets are:")
        pprint.pprint(response)
    except ClientError as e:
        logging.error(e)

def get_bucket_versioning(bucket_name):
    s3_client = boto3.client('s3')
    response = s3_client.get_bucket_versioning(Bucket=bucket_name)
    logging.info(f"listing {bucket_name} versioning info")
    pprint.pprint(response)

    # empty response means versioning is not activated or setted yet

def set_bucket_versioning(bucket_name):
    s3_client = boto3.client('s3')
    response = s3_client.put_bucket_versioning(Bucket=bucket_name, VersioningConfiguration={
        'MFADelete': 'Disabled',
        'Status': 'Enabled'
    })
    logging.info(f"setting {bucket_name} versioning to Enabled")
    pprint.pprint(response)




logging.getLogger().setLevel(logging.INFO)

#list_buckets()

#set_bucket_versioning('senko-learning-aws-test1')

#get_bucket_versioning('senko-learning-aws-test1')
