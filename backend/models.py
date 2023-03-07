from django.db import models

# Create your models here.

class admindb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    EMAIL = models.EmailField(null=True, blank=True)
    NUMBER = models.IntegerField(null=True, blank=True)
    USERNAME = models.CharField(max_length=50, null=True, blank=True)
    PASSWORD = models.CharField(max_length=50, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile",null=True, blank=True)

class categorysave(models.Model):
    Name=models.CharField(max_length=100, null=True, blank=True)
    Description=models.CharField(max_length=100, null=True, blank=True)
    Image=models.ImageField(upload_to="profile",null=True, blank=True)

class proDetails(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField( null=True, blank=True)
    Quantity = models.IntegerField( null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)