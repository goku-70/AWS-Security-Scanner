#Script to list access keys
import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta
results = []
def scan():
    iam = boto3.client('iam')
    for user in iam.list_users()['Users']:
        user = user['UserName']
        access_keys = iam.list_access_keys(UserName=user)
        print(access_keys)

scan()
