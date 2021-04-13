#!/usr/bin/env python
# coding: utf-8

# In[104]:


import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta


# In[105]:


result = []


# In[128]:


def scan():

    client = boto3.client('ec2')
    try:
        response = client.describe_security_groups()
        for securitygroup in response['SecurityGroups']:
            print("Security_Group_ID: {}, Group_Name: {}, Ip_Permissions: {}" 
                  
                  .format(
                        securitygroup['GroupId'], 
                        securitygroup['GroupName'], 
                        securitygroup['IpPermissions']
                        ))
            
    except Exception as E:
            print(E)
            
scan()


# In[ ]:




