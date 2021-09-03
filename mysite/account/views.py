from django .http import HttpResponse
from django.shortcuts import render
from account.models import Account

# Create your views here.
def insert(request):
    accountno=int(request.GET["accountno"])
    accountname=input(request.GET["accountname"])
    accountid=int(request.GET["accountid"])
    accounttype=input(request.GET["accounttype"])
    accountbalance=int(request.GET["accountbalance"])
    account=Account(accountno=accountno,accountname=accountname,accountid=accountid,accounttype=accounttype,accountbalance=accountbalance)
    account.save()
    return render(request,"insert.html", HttpResponse("Inserted"))

    
    
def delete(request):
    account=Account.objects.filter(accountid=125)
    if len(account)==0:
            return HttpResponse("none")
    else:
            account[0].delete()
            return HttpResponse("Delete name="+str(account[0].accounttype)) 

def find(request):
    account=Account.objects.filter(accountname="manjit saxena")& Account.objects.filter(accountid=155)
    if len(account)==0:
            return HttpResponse("none")
    else:
            
            return HttpResponse("Find name="+str(account[0].accountid))

def database(request):
    
    accountno=""
    accountname=""
    accountid=""
    accounttype=""
    accountbalance=""
    cmd=""
    result=""
    if request.GET:
       cmd= request.GET["command"]
    if cmd=="Insert":
       accountno=request.GET["accountno"]
       accountname=request.GET["accountname"]
       accountid=request.GET["accountid"]
       accounttype=request.GET["accounttype"]
       accountbalance=request.GET["accountbalance"] 
       account=Account(accountno=accountno,accountname=accountname,accountid=accountid,accounttype=accounttype,accountbalance=accountbalance)
       account.save()
       result="Inserted Succesfully"
    if cmd=="search":
        accountno=request.GET["accountno"]
        account=Account.objects.filter(accountno=accountno)
        if len(account)==0:
            result="no data found"
        else:
            accountno=account[0].accountno       
            accountname=account[0].accountname
            accountid=account[0].accountid
            accounttype=account[0].accounttype
            accountbalance=account[0].accountbalance 
            result="search succesfull" 
    if cmd=="Delete":
        accountno=request.GET["accountno"]
        account=Account.objects.filter(accountno=accountno)
        if len(account)==0:
            result="no data found"
        else:
            accountno=account[0].accountno       
            accountname=account[0].accountname
            accountid=account[0].accountid
            accounttype=account[0].accounttype
            accountbalance=account[0].accountbalance
            account[0].delete()
            result="delete succesfull"
    if cmd=="Update":
        accountno=request.GET["accountno"]
        account=Account.objects.filter(accountno=accountno)
        if len(account)==0:
            result="not data found"
        else:
            account[0].accountno=request.GET["accountno"]
            account[0].accountname=request.GET["accountname"]
            account[0].accountid=request.GET["accountid"]
            account[0].accounttype=request.GET["accounttype"]
            account[0].accountbalance=request.GET["accountbalance"]
            account[0].save()
            result="update succesfull"
       
    data={"result":result,"accountno":accountno,"accountname":accountname,"accountid":accountid,"accounttype":accounttype,"accountbalance":accountbalance}
    return render(request,"insert.html",{"data":data})
