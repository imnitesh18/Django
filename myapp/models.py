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
  
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=50)
    salary = models.IntegerField()
    def _str_(self):
        return self.name

class Section(models.Model):
    section_name= models.CharField(max_length=50)
    no_of_students=models.IntegerField()
    faculty=models.ForeignKey(Faculty, on_delete=models.CASCADE) 
    def _str_(self):
        return self.section_name

class Blogpost(models.Model):
  post_id=models.AutoField(primary_key=True)
  title=models.CharField(max_length=30)
  post=models.TextField()
  thumbnail=models.ImageField(upload_to='images/')
  def __str__(self):
     return self.title
  


from django.db import models

class Cookie(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)



     


