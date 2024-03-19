from django.db import models

# Create your models here.
class Emp(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  slary=models.IntegerField()

