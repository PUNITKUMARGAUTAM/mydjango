"""
DJango technology den=monstrator project. Strictly for learning and experimenting

"""

from django.http import HttpResponse
#This library is used for sending html strings to the output i,e browser
from django.shortcuts import render
#this functien sends a html template to the output. 
import  requests
#Used for accessing http resources from the internet
import  json
#Parsing JSON and also creating JSON
# Create your views here.
def weather(request):
#Calling the openweather api via a python program.
#The api is hosted at https://api.openweathermap.org/
    appid="fakeid"
    city=""
    code=""
    result=""
    temp=""
    humidity=""
    
        if not request.GET:
            data={"city":city}
            return render(request,"weather.html",{"data":data})
        if request.GET:
            city=request.GET["city"]
#This is the actual api call being made. It gets the live weather info from the api
            url="https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid,city)
            response=requests.get(url)
            code=response.status_code
        if code!=200:
            result="Your searching City Name is not found"
        else:
            jsondata=json.loads(response.text)
            temp=jsondata["main"]["temp"]
            humidity=jsondata["main"]["humidity"]
   
    data={"result":result,"city":city,"temp":temp,"humidity":humidity}
    
    
    
    
    return render(request,"weather.html",{"data":data})
   
