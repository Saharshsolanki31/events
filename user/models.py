from django.db import models

# Create your models here.
from django.db.models import Model


class User(Model):
    name=models.CharField(max_length=200)
    number=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    college_name=models.CharField(max_length=200)
    link=models.CharField(max_length=1000,blank=True,null=True)
    file=models.FileField(upload_to='static/files',null=True,blank=True)
    def __str__(self):
        return self.email

