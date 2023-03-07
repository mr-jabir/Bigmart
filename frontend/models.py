from django.db import models

# Create your models here.

class CustRegdb(models.Model):
    USERNAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.EmailField(null=True, blank=True)
    PASSWORD = models.CharField(max_length=50, null=True, blank=True)
    CONPWD = models.CharField(max_length=50, null=True, blank=True)
