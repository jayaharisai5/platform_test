from rest_framework import serializers
from data.models import UserAwsCredentials, UserAwsObject

class UserAwsCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAwsCredentials
        fields="__all__"

class UserAwsObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAwsObject
        fields="__all__"