from django.db import models

# Create your models here.
class BookModel(models.Model):

    questions = models.CharField(max_length=300)
    bname = models.CharField(max_length= 50)
    bid = models.CharField(max_length= 50)
    bauthor= models.CharField(max_length= 50)
    bprice = models.CharField(max_length= 50)

class Meta:
    db_table = "Book library"