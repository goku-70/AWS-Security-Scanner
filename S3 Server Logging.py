#!/usr/bin/env python
# coding: utf-8

# In[2]:


import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta


# In[3]:


s3client = boto3.client('s3')


# In[4]:


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


# In[ ]:




