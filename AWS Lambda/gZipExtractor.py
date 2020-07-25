import json
import boto3
import gzip
from io import BytesIO

''' 
This script reads in events when any files touches the s3 bucket. If that file has .gzip extension
then lambda automatically grabs the file using boto3. Itextracts the file via gzip and deletes the .gzip file again using boto3.

'''


def lambda_handler(event, context):
    bucket = event[“Records”][0][‘s3’][‘bucket’][‘name’]
    key = event[“Records”][0][‘s3’][‘object’][‘key’]
    s3 = boto3.client(‘s3’)
    new_key = key[:-3]

    s3.upload_fileobj(
        Fileobj=gzip.GzipFile(
            None,
            ‘rb’,
            fileobj=BytesIO(
                s3.get_object(Bucket=bucket, Key=key)[‘Body’].read())),
        Bucket=bucket,
        Key=new_key)

    s3r = boto3.resource(“s3”)
    s3r.Object(bucket, key).delete()