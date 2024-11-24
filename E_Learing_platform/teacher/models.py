from django.db import models
from student.models import quires
from home.models import course
# Create your models here.





class qanswers(models.Model):
    ques = models.ForeignKey(quires,on_delete=models.CASCADE)
    answer = models.TextField(blank=True)
    a_img = models.ImageField(upload_to='qu_img',blank=True)
    def __str__(self):
        return self.ques.Question
    

class lecture(models.Model):
    subject = models.ForeignKey(course, on_delete=models.CASCADE)
    link = models.CharField(max_length=1000,null=True)
    time = models.CharField(max_length=1000,null=True)
    chapter = models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.subject.product_name +"---"+ self.chapter
    

class assignment(models.Model):
    subject = models.ForeignKey(course,on_delete=models.CASCADE)
    assignment_name = models.CharField(max_length=1000,null=True)
    assignment_file = models.FileField(upload_to="teacher_data",null=True)
    def __str__(self):
        return self.subject.product_name +"---"+ self.assignment_name
    

class notes(models.Model):
    subject = models.ForeignKey(course,on_delete=models.CASCADE)
    notes_name = models.CharField(max_length=1000,null=True)
    notes_file = models.FileField(upload_to="teacher_data",null=True)
    def __str__(self):
        return self.subject.product_name +"---"+ self.notes_name
    

