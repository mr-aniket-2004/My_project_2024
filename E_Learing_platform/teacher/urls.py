from django.contrib import admin
from django.urls import path
from teacher import views
# from home import views


urlpatterns = [
   path("/teacher",views.index1,name='teacherdashboard'),
   path("/assignment",views.assignment1,name='teacherassignment'),
   path("/assignment/addlecture",views.addlecture,name='addlecture'),
   path("/assignment/addassignment",views.addassignment,name='addassignment'),
   path("/assignment/addnotes",views.addnotes,name='addnotes'),
   path("/chat",views.chat,name='teacherchat'),
   path("/profile",views.profile,name='teacherprofile'),
   path("/profile/change-password",views.changepassword,name='changepassword'),
   
#    path("log",views.student_logout,name='log'),
]