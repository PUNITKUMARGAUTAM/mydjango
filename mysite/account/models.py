from django.db import models

# Create your models here.
class Account(models.Model):
    accountno = models.CharField(max_length = 300)
    accountname = models.CharField(max_length = 50)
    accountid = models.CharField(max_length = 50)
    accounttype = models.CharField(max_length = 50)
    accountbalance = models.CharField(max_length = 50)

class Meta:
    db_table = "accounts"