from django.http import HttpResponse
from django.shortcuts import render
from MCQ.models  import Quiz

# Create your views here:


def testquiz(request):
    Qustno=""
    Qustn=""
    OptA=""
    optB=""
    OPtC=""
    OptD=""
    RightAns=""
    cmd="new"
    if not request.GET:
        data={"cmd":cmd,"Qustno":0}
        return render(request,"mcq2.html",{"data":data})
    else:
        cmd=request.GET["command"]
        if cmd=="Prev":
            Qustno=int(request.GET["Qustno"])
            Qustno-=1
            MCQ=Quiz.objects.filter(Qustno=Qustno)
            data={"cmd":cmd,"Qustno":Qustno,"q":MCQ[0]}
            return render(request,"mcq2.html",{"data":data})
         
        if cmd=="Next":
            Qustno=int(request.GET["Qustno"])
            Qustno+=1
            MCQ=Quiz.objects.filter(Qustno=Qustno)       
            data={"cmd":cmd,"Qustno":Qustno,"q":MCQ[0]}
            return render(request,"mcq2.html",{"data":data})
        
        
   
      


        
    
               
                
