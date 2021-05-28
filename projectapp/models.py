from django.db import models

# Create your models here.
class reg_table(models.Model):
	Name=models.CharField(max_length=100,default='')
	Email=models.CharField(max_length=100,default='')
	Password=models.CharField(max_length=100,default='')
	Mobile=models.CharField(max_length=100,default='')
	State=models.CharField(max_length=100,default='')
	Dist=models.CharField(max_length=100,default='')
	City=models.CharField(max_length=100,default='')
	Status=models.CharField(max_length=100,default='0')
class login_table(models.Model):
	Username=models.CharField(max_length=100,default='')
	Password=models.CharField(max_length=100,default='')