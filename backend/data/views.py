from django.shortcuts import render
from data import models 
from data.serializer import UserAwsCredentialsSerializer, UserAwsObjectsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import boto3
import pandas as pd

# Create your views here.
@api_view(["POST"])
def s3(request):
    if request.method == "POST":
        collect_details = UserAwsCredentialsSerializer(data=request.data)
        if collect_details.is_valid():
            try:
                s3 = boto3.resource(
                            's3',
                            aws_access_key_id=collect_details.data["aws_access_key_id"],
                            aws_secret_access_key=collect_details.data["aws_secret_access_key"],
                            region_name=collect_details.data["region_name"]

                    )
                request.session['aws_access_key_id'] = collect_details.data["aws_access_key_id"]
                request.session['aws_secret_access_key'] = collect_details.data["aws_secret_access_key"]
                request.session['region_name'] = collect_details.data["region_name"]
                request.session['bucket_name'] = collect_details.data["bucket_name"]
                print("Sucessfully connected")
            except:
                print("Not connected")  

            print(buckets(request))


            return Response(collect_details.data, status=status.HTTP_201_CREATED)
            return Response(collect_details.data, status=status.HTTP_400_BAD_REQUEST)

def buckets(request):
    if request.session.has_key("aws_access_key_id"):
        aws_access_key_id = request.session['aws_access_key_id']
        if request.session.has_key("aws_secret_access_key"):
            aws_secret_access_key = request.session['aws_secret_access_key']
            if request.session.has_key("region_name"):
                region_name = request.session['region_name']
                if request.session.has_key("bucket_name"):
                    bucket_name = request.session['bucket_name']
                    
                    s3 = boto3.resource(
                                            's3',
                                            aws_access_key_id=aws_access_key_id,
                                            aws_secret_access_key=aws_secret_access_key,
                                            region_name=region_name

                                    )
    object = []
    for obj in s3.Bucket(bucket_name).objects.all():
        object.append(obj.key)
    
    return object

@api_view(["POST"])
def s3_show_csv(request):
    if request.method == "POST":
        collect_object = UserAwsObjectsSerializer(data=request.data)
        if collect_object.is_valid():
            if request.session.has_key("aws_access_key_id"):
                aws_access_key_id = request.session['aws_access_key_id']
                if request.session.has_key("aws_secret_access_key"):
                    aws_secret_access_key = request.session['aws_secret_access_key']
                    if request.session.has_key("region_name"):
                        region_name = request.session['region_name']
                        if request.session.has_key("bucket_name"):
                            bucket_name = request.session['bucket_name']
                            
                            s3 = boto3.resource(
                                                    's3',
                                                    aws_access_key_id=aws_access_key_id,
                                                    aws_secret_access_key=aws_secret_access_key,
                                                    region_name=region_name

                                            )
    obj = s3.Bucket(bucket_name).Object(collect_object.data['object']).get()
    foo = pd.read_csv(obj['Body'], index_col=0)
    print(foo)
    return Response(foo)

