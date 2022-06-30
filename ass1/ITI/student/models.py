from django.db import models

# Create your models here.
class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    usernamfrom django.db import models

# Create your models here.
class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    username =models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    email=models.EmailField(max_length=50)

class student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)


class courses(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    user = models.ForeignKey(MyUser, null=False, on_delete=models.CASCADE)
