# coding: utf-8
import boto3
client = boto3.client('rekognition', 'eu-west-1')
resp = client.detect_labels(Image={'S3Object': {'Bucket': 'talentsprint-dviz', "Name": "elephants.jpeg"}})
print(resp['Labels'])
