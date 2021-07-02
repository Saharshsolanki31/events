from django.db import models

# Create your models here.
from django.db.models import Model


class ManagerLogin(Model):
    userid=models.CharField(max_length=520)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.userid
