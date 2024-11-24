from django.db import models
from django.contrib.auth.models import User
from home.models import course
from django.db.models.signals import pre_save
# Create your models here.

from home.models import course 


class student_couser(models.Model):
    # core_subject = models.OneToOneField(course,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.core_subject.product_name
    

class usercourse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sub = models.ForeignKey(course,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.first_name+""+ self.sub.product_name
    
class helpquary(models.Model):
    student_name=models.CharField(max_length=500)
    student_email =models.CharField(max_length=300)
    student_message = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    

class quires(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    Question = models.TextField(blank=True)
    q_img = models.ImageField(upload_to='qu_img' , blank=True)
    # Answer = models.TextField(blank=True)
    # a_img = models.ImageField(upload_to='qu_img',blank=True)
    def __str__(self):
        return self.student.first_name +"----"+ self.Question




