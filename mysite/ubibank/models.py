from django.db import models

# Create your models here.
class Bank(models.Model):
    Acno = models.CharField(max_length = 100)
    Acname = models.CharField(max_length = 50)
    Actype = models.CharField(max_length = 50)
    Acbal = models.CharField(max_length = 50)
    Acmbno = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    
class Meta:
      db_table="Bank Details"    
    