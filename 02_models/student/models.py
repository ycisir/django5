from django.db import models

class Profile(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	roll = models.IntegerField()
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=70)
