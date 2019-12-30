from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class events(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	lat = models.FloatField()
	lan = models.FloatField()
	event_type = models.CharField(max_length=20)

class users(AbstractUser):
	pass
	mobileno = models.IntegerField()