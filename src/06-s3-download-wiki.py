#!/usr/bin/env/python
import os
import boto3
from botocore.client import Config

s3 = boto3.resource('s3',
                    endpoint_url=os.getenv('S3_ENDPOINT_URL', 'https://s3.amazon.com'),
                    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', None),
                    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', None)
                    )

print('Existing buckets:')

for bucket in s3.buckets.all():
        print(bucket.name)

print('Downloading parquet data file...')
s3.Bucket(bucket.name).download_file('data/wiki_simple_100k.parquet', 'data/wiki_simple_100k.parquet')
