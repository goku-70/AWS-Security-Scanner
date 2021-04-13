#Script to check if S3 Bucket Server Logging is Enabled or Disabled
import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta
s3client = boto3.client('s3')
def scan():
    results = []
    s3 = boto3.client('s3')
    for bucket in s3.list_buckets()['Buckets']:
        bucket = bucket['Name']
        response = s3.get_bucket_logging(Bucket=bucket)
        if 'LoggingEnabled' in response:
            results.append({
                'BucketName': bucket,
                'ServerLogging': 'Server Logging is Enabled'
            })
        else:
            results.append({
                'BucketName': bucket,
                'ServerLogging': 'Server Logging is Disabled'
            })
    print(results)
    
scan()
