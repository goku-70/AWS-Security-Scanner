#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta


# In[2]:


results = []


# In[3]:


def scan():
    s3 = boto3.client('s3')

    bucket_list = s3.list_buckets()
    for bucket in bucket_list['Buckets']:
        try:
            enc = s3.get_bucket_encryption(Bucket=bucket['Name'])
            rules = enc['ServerSideEncryptionConfiguration']['Rules']
            results.append({
                'BucketName': bucket['Name'],
                'Encryption': enc['ServerSideEncryptionConfiguration']['Rules']
            })
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                results.append({
                'BucketName': bucket['Name'],
                'Encryption': 'No Server-Side Encryption'
            })
            else:
                results.append({
                'BucketName': 'Unexpected Error',
            })
    print(results)


scan()


# In[ ]:




