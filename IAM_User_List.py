#Script to check IAM User List
import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta
results = []
def scan():
    iam = boto3.client('iam')
    
    user_list = iam.list_users()

    print(user_list)
scan()
