from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
	FullName = models.CharField(max_length = 50)
	Email  =  models.EmailField(primary_key = True, unique = True,max_length = 100)
	Gender = models.CharField(max_length = 10)
	PhoneNumber = models.IntegerField(unique = True)
	Qualification = models.CharField(max_length = 50)
	Branch = models.CharField(max_length =  100)
	password = models.CharField(max_length = 25)
	conPassword = models.CharField(max_length = 25)


class login(models.Model):
	Username = models.EmailField(max_length = 100, primary_key = True)
	password = models.CharField(max_length = 25)
