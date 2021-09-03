from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    html = "<h1>Default View</h1>"
    return HttpResponse(html)
def hello(request):
    return HttpResponse("Hello")    
def manas(request):
    return HttpResponse("Chai☕")
def manjit(request):
    return HttpResponse("company")
def ADD(request):
    a=0
    b=0
    if request.GET:
        a=int(request.GET["a"])
        b=int(request.GET["b"])
    sum=a + b
    data={"a":a,"b":b,"sum":sum}
    return render(request,"getform.html",{"data":data})

def sum(request):
    a=0
    b=0
    if request.POST:
        a=int(request.POST["a"])
        b=int(request.POST["b"])
    sum=a + b
    data={"a":a,"b":b,"sum":sum}
    return render(request,"postform.html",{"data":data})
    
def calculator(request):
    a=0
    b=0
    result=""
    cmd=""
    if request.GET:
       cmd=request.GET["command"]
       a=int(request.GET["a"])
       b=int(request.GET["b"])
    if cmd=="subtraction":
       result=a - b
    if cmd=="addition":
       result=a + b
    if cmd=="divide":
       result=a/b 
    if cmd=="multiplication":
       result=a*b
    data={"a":a,"b":b,"result":result}
    return render(request,"calculator.html",{"data":data})   
def calculator1(request):
    a=0
    b=0
    result=""
    cmd=""
    try:
        try:
            print(type(request.GET))
            cmd=request.GET["command"]
        except:
            cmd="sub"

        a=int(request.GET["a"])
        b=int(request.GET["b"])
        if cmd=="sub":
           result=a - b
        if cmd=="add":
           result=a + b
        if cmd=="div":
           result=a/b 
        if cmd=="mul":
           result=a*b    
        data={"a":a,"b":b,"result":result} 
        return render(request,"calculator1.html",{"data":data})
            
        
    except ZeroDivisionError as z:
        
        data={"a":a,"b":b,"result":str(z)}
        return render(request,"calculator1.html",{"data":data})           

             
           