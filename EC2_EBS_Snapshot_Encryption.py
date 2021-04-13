#Script to check EBS snapshot encrypted or not
import boto3
from botocore.exceptions import ClientError
from datetime import timezone, date, datetime, timedelta
assets_data_output = []
issues_data_output = []
events_data_output = []
def scan():
    # Init EC2 boto3 client
    # We'll need to loop through every region
    client = boto3.client('ec2', region_name="us-east-1")
    
    # Get EBS Snapshots
    paginator = client.get_paginator(
        'describe_snapshots').paginate(OwnerIds=['self'])

    for ebs_snapshots in paginator:
        for snapshot in ebs_snapshots['Snapshots']:

            # Append each EBS Snapshot as a vectrix asset
            assets_data_output.append({
                'id': snapshot['SnapshotId'],
                'type': 'aws_ebs_snapshot',
                'display_name': 'Snapshot: ' + snapshot['SnapshotId'],
                'metadata': {
                    'volume_id': {
                        'priority': 50,
                        'value': snapshot['VolumeId']
                    },
                    'volume_size': {
                        'priority': 50,
                        'value': snapshot['VolumeSize']
                    },
                    'description': {
                        'priority': 50,
                        'value': snapshot['Description']
                    }
                }
            })

            # Identify EBS Snapshot Unencrypted Issue
            if snapshot['Encrypted'] is False:
                issues_data_output.append({
                    'issue': 'EC2 EBS Snapshot Unencrypted',
                    'asset_id': snapshot['SnapshotId'],
                    'metadata': {}
                })
        return assets_data_output, issues_data_output
scan()
