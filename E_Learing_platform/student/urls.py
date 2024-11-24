from django.contrib import admin
from django.urls import path
from student import views
# from home import views


urlpatterns = [
   path("/student",views.index1,name='dashboard'),
   path("/feedback",views.feedback_info, name="feedback_info"),
   path("/course",views.student_cour, name="student_course"),
   path("/course/temp",views.temp , name='temp'),
   path("/course/temp/<slug>",views.temp , name='temp'),
   # path("/course/temp/<slug>",views.course_model , name='course_model'),
   path("/course/temp/checkout/<slug:slug>",views.checkout,name="checkout"),
   path("/assignment",views.assignment1,name="assignment"),
   path("/chat",views.chat,name="chat"),
   path("/help",views.help,name="help"),
   path("/profile",views.profile,name="profile"),
   path("/course/mycourse",views.mycourse,name="mycourse"),
   path("/course/mycourse/download/<slug>",views.download,name="download"),
   path("/course/mycourse/temp/<slug>",views.course_model, name='course_model'),
   path("/course/mycourse/temp/learingpage1/<slug>",views.chapter_video1, name='chapter_video1'),
   path("/course/mycourse/temp/learingpage2/<slug>",views.chapter_video2, name='chapter_video2'),
   path("/course/mycourse/temp/learingpage3/<slug>",views.chapter_video3, name='chapter_video3'),
   path("/course/mycourse/temp/learingpage4/<slug>",views.chapter_video4, name='chapter_video4'),
   path("/course/mycourse/temp/learingpage5/<slug>",views.chapter_video5, name='chapter_video5'),
   path("/course/mycourse/temp/quiz/<slug>",views.quizpage, name='quiz'),
   path("/upgrade",views.upgrade,name="upgrade"),
   path("/upgrade/payment/",views.success,name="payment"),
   path("/profile/change-password",views.changepassword,name='changepassword'),
   
#    path("log",views.student_logout,name='log'),
]