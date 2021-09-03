from django.http import HttpResponse
from django.shortcuts import render
from ubibank.models import Bank 

# Create your views here.

def UBI(request):
    
    Acno=""
    Acname=""
    Actype=""
    Acbal=""
    Acmbno=""
    email=""
    cmd=""
    result=""
    if request.GET:
       Acno=request.GET["Acno"]
       Acname=request.GET["Acname"]
       Actype=request.GET["Actype"]
       Acbal=request.GET["Acbal"]
       Acmbno=request.GET["Acmbno"]
       email=request.GET["email"]       
       ubibank=Bank(Acno=Acno,Acname=Acname,Actype=Actype,Acbal=Acbal,Acmbno=Acmbno,email=email)
       ubibank.save()
       result="Inserted Succesfully"
    data={"result":result,"Acno":Acno,"Acname":Acname,"Actype":Actype,"Acbal":Acbal,"Acmbno":Acmbno,"email":email}   
    return render(request,"Home.html",{"data":data})
    
def withdrawl(request):
    Acno=""
    Acname=""
    Actype=""
    Acbal=""
    Acmbno=""
    email=""
    cmd=""
    result=""
    if request.GET:
        cmd=request.GET["command"]
    if cmd=="search":
        Acno=request.GET["Acno"]
        ubibank=Bank.objects.filter(Acno=Acno)
        if len(ubibank)==0:
            result="no data found"
        else:
            Acno=ubibank[0].Acno
            Acname=ubibank[0].Acname
            Actype=ubibank[0].Actype
            Acbal=ubibank[0].Acbal
            Acmbno=ubibank[0].Acmbno
            email=ubibank[0].email
            ubibank[0].save()
            result="Search sucess" 
        data={"result":result,"Acno":Acno,"Acname":Acname,"Actype":Actype,"Acbal":Acbal,"Acmbno":Acmbno,"email":email}   
        return render(request,"withdrawl.html",{"data":data})     
    
    if cmd=="withdrawl":
        Acno=request.GET["Acno"]
        ubibank=Bank.objects.filter(Acno=Acno)
        if len(ubibank)==0:
            result="no data found"
        else:
            
            Acname=ubibank[0].Acname
            Actype=ubibank[0].Actype
            amount=int(request.GET["amount"])
            ubibank[0].Acbal=str(int(ubibank[0].Acbal)-amount)
            Acbal=ubibank[0].Acbal
            Acmbno=ubibank[0].Acmbno
            email=ubibank[0].email
            ubibank[0].save()
            result="withdrawl success"         
        data={"result":result,"Acno":Acno,"Acname":Acname,"Actype":Actype,"Acbal":Acbal,"Acmbno":Acmbno,"email":email}   
        return render(request,"withdrawl.html",{"data":data})     
    
        
        
def deposite(request):
    Acno=""
    Acname=""
    Actype=""
    Acbal=""
    Acmbno=""
    email=""
    cmd=""
    result=""
    if request.GET:
        cmd=request.GET["command"]
    if cmd=="search":
        Acno=request.GET["Acno"]
        ubibank=Bank.objects.filter(Acno=Acno)
        if len(ubibank)==0:
            result="no data found"
        else:
            Acno=ubibank[0].Acno
            Acname=ubibank[0].Acname
            Actype=ubibank[0].Actype
            Acbal=ubibank[0].Acbal
            Acmbno=ubibank[0].Acmbno
            email=ubibank[0].email
            ubibank[0].save()
            result="Search sucess" 
        data={"result":result,"Acno":Acno,"Acname":Acname,"Actype":Actype,"Acbal":Acbal,"Acmbno":Acmbno,"email":email}   
        return render(request,"deposite.html",{"data":data})     
    
    if cmd=="deposite":
        Acno=request.GET["Acno"]
        ubibank=Bank.objects.filter(Acno=Acno)
        if len(ubibank)==0:
            result="no data found"
        else:
            
            Acname=ubibank[0].Acname
            Actype=ubibank[0].Actype
            amount=int(request.GET["amount"])
            ubibank[0].Acbal=str(int(ubibank[0].Acbal)+amount)
            Acbal=ubibank[0].Acbal
            Acmbno=ubibank[0].Acmbno
            email=ubibank[0].email
            ubibank[0].save()
            result="deposite success"         
        data={"result":result,"Acno":Acno,"Acname":Acname,"Actype":Actype,"Acbal":Acbal,"Acmbno":Acmbno,"email":email}   
        return render(request,"deposite.html",{"data":data})     
    
        
    