from django.db import models

# Create your models here.

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField(max_length=2)
