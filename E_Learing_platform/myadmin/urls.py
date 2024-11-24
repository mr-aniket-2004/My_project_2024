from django.contrib import admin
from django.urls import path ,include
from myadmin import views

urlpatterns = [
   path("",views.myadmin, name="admindesh"),
   path("admindash",views.admindash,name="admindashboard"),
   path("course/",views.allcourse, name="allcourse"),
]