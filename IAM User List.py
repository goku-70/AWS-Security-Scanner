#!/usr/bin/env python
# coding: utf-8

# In[23]:


import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta


# In[24]:


results = []


# In[27]:


def scan():
    iam = boto3.client('iam')
    
    user_list = iam.list_users()

    print(user_list)
scan()


# In[ ]:




