from django.db import models

# Create your models here.
class MobileBrand(models.Model):
    mobilesplus = models.CharField(max_length = 300)
    mobilesrealme = models.CharField(max_length = 50)
    mobilesredmi = models.CharField(max_length = 50)
    mobilesapple = models.CharField(max_length = 50)
class Meta:
    db_table = "Mobiles"

