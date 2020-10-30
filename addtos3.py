import boto3
import boto3.s3
import sys

KEY_NAME_FOR_FILE = 'junk file'
AWS_SECRET_ACCESS_KEY = ''

bucket_name = 'syllabus-repository'

testfile = ''

s3 = boto3.resource('s3')

s3.meta.client.upload_file(testfile, bucket_name, KEY_NAME_FOR_FILE, ExtraArgs={'ACL':'public-read'})