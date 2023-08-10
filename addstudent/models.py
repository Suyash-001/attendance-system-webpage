from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    enrollment=models.CharField(primary_key='True',max_length=50)
    course=models.CharField(max_length=128)
    year=models.CharField(max_length=50)
    semester=models.CharField(max_length=50)
    attendance=models.BooleanField(default="False")
    def __str__(self):
        return self.name
