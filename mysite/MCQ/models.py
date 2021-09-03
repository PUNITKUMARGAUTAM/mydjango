from django.db import models

# Create your models here.

class Quiz(models.Model):
    Qustno=models.CharField(max_length = 300)
    Qustn = models.CharField(max_length = 200)
    OptA = models.CharField(max_length = 200)
    optB = models.CharField(max_length = 200)
    OptC = models.CharField(max_length = 200)
    OptD = models.CharField(max_length = 200)
    RightAns=models.IntegerField()
    
    class Meta:
      db_table="questions" 