#Script to check EKS Cluster List
import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta
assets_data_output = []
issues_data_output = []
events_data_output = []
def scan():
    
    client = boto3.client('eks', region_name="us-east-1")
    clusterlist = client.list_clusters()
    empty = clusterlist['clusters']
    for item in range(len(empty)):
        clusterdata = client.describe_cluster(name=empty[item])
        return clusterdata['cluster']
scan()
