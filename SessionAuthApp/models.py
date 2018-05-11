from django.db import models

# Create your models here.
class Stud(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=10)
    marks=models.IntegerField()