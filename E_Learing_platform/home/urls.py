from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
    path("",views.index, name= "home"),
    path("home",views.index, name="home"),
    path("about",views.course1, name= "about"),
    path("community",views.community, name= "community"),
    path("contact-us",views.contactus, name= "contact-us"),
    path("log",views.log, name= "log"),
    path("sign",views.sign, name= "sign"),
    path("python",views.python,name="python"),
    path("java",views.java,name="java"),
    path("check_user",views.check_user,name="check_user"),
    path("student",include('student.urls')),
    path("teacher",include('teacher.urls')),
    path("logout",views.student_logout,name="logout"),
    # path("update",views.update_info, name="update_info")
]
# urlpatterns = [
#     path("",views.index, name= "home"),
#     path("home/",views.index, name="home"),
#     path("about/",views.course, name= "about"),
#     path("community/",views.community, name= "community"),
#     path("contact-us/",views.contactus, name= "contact-us"),
#     path("log/",views.log, name= "log"),
#     path("python/",views.python,name="python"),
#     path("java/",views.java,name="java")
# ]
