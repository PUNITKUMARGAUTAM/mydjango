from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book

# Create your views here.
def insert(request):
    questions="book1"# request.GET["bookname"]
    bname="python"#request.GET["subject"]
    bid="125"
    bauthor="manjit"
    bprice=555
    print(questions,bname,bid,bauthor,bprice)
    book=Book(
    questions=book1,bname=python,bid=125,bauthor=manjit,bprice=555
    )
    book.save()
    return HttpResponse("Inserted")

