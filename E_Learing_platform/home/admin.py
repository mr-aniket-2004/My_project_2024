from django.contrib import admin
from home.models import Contact,course,sign_up_table,notification,free_course,QuesModel,completeCourse
# from student.models import student_couser
# Register your models here.
admin.site.register(Contact)
admin.site.register(course)
admin.site.register(sign_up_table)
admin.site.register(notification)
admin.site.register(free_course)
admin.site.register(QuesModel)
admin.site.register(completeCourse)
# admin.site.register(course_info)