from django.db import models

# Create your models here.
class Emp(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  salary=models.IntegerField()


class SignUp(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
  
class Customers(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
  


