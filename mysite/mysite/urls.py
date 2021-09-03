"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from account import views as vw
from ubibank import views as v
from MCQ import views as vs
from weather import views as w

urlpatterns = [
    path('admin/', admin.site.urls),
path("hello/",views.hello),
path("manas/",views.manas),
path("manjit/",views.manjit),
path("ADD/",views.ADD),
path("sum/",views.sum),
path("calculator/",views.calculator),
path("calculator1/",views.calculator1),
path("insert/",vw.insert),
path("delete/",vw.delete),
path("find/",vw.find),
path("database/",vw.database),
path("UBI/",v.UBI),
path("withdrawl/",v.withdrawl),
path("deposite/",v.deposite),
path("testquiz/",vs.testquiz),
path("weather/",w.weather),
path("",views.index),

]
