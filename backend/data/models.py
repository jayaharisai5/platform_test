from django.db import models

# Create your models here.
class UserAwsCredentials(models.Model):
    aws_access_key_id = models.CharField(max_length=250)
    aws_secret_access_key = models.CharField(max_length=250)
    region_name = models.CharField(max_length=250)
    bucket_name = models.CharField(max_length=250)

class UserAwsObject(models.Model):
    object = models.CharField(max_length=500)