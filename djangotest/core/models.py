from django.db import models

# Create your models here.

class User(models.Model):
	user_types = (
		('st','Student'),
		('fc','Faculty')
	)
	dept_type = (
		('ece', 'Electronics'),
		('ele', 'Electrical'),
		('mec', 'Mechanical'),
		('civ', 'Civil'),
		('com', 'Computers'),
	)
	username = models.CharField(max_length = 100, unique = True, null=True, blank=True)
	email = models.CharField(max_length=50, unique=True, null=True, blank=True)
	password = models.CharField(max_length = 100)
	full_name = models.CharField(max_length = 255)
	user_type = models.CharField(max_length=100, choices=user_types, default='st')
	dept = models.CharField(max_length=25, choices=dept_type, default='ece')

