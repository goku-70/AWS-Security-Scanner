#!/usr/bin/env python
# coding: utf-8

# In[13]:


import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta


# In[14]:


results = []


# In[22]:


def scan():
    s3 = boto3.client('s3')
    
    bucket_list = s3.list_buckets()
    for bucket in s3.list_buckets()['Buckets']:
        bucket = bucket['Name']
        response = s3.get_bucket_versioning(Bucket=bucket)
    if 'Status' in response and response['Status'] == 'Suspended':
        results.append({
            'BucketName': bucket,
            'Versinoning': 'Suspended'
        })

    elif 'Status' in response and response['Status'] == 'Enabled': 
        results.append({
            'BucketName': bucket,
            'Versinoning': 'Enabled'
        })
    else:
        results.append({
            'BucketName': bucket,
            'Versinoning': 'Not found'
        })
    print(results) 

scan()


# In[ ]:




