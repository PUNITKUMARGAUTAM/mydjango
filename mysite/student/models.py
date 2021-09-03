from django.db import models

# Create your models here.
class Student(models.Model):
    studentrollno = models.CharField(max_length= 300)
    studentname = models.CharField(max_length= 50)
    studentbranch = models.CharField(max_length= 50)
    studentdpt = models.CharField(max_length= 50)

class Meta:
    db_table = "student"
