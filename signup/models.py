from django.db import models

# Create your models here.
class signup(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=128)
    confirm_password=models.CharField(max_length=128)