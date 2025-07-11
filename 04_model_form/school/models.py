from django.db import models

class Profile(models.Model):
	teacher_name = models.CharField(max_length=50)
	student_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
