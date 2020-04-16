from django.db import models

# Create your models here.
class user(models.Model):
	email=models.EmailField(max_length=254)
	subject=models.CharField(max_length=254)
	text=models.CharField(max_length=400000)
