from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from autoslug import AutoSlugField

# Create your models here.
class Contact(models.Model):
    fname= models.CharField(max_length=120)
    sname= models.CharField(max_length=120)
    email= models.CharField(max_length=120)
    phoneno = models.CharField(max_length=15)
    desc = models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.fname

class course(models.Model):
    product_name= models.CharField(max_length=200)
    price =models.CharField(max_length=100)
    img =models.ImageField(upload_to='img')
    duration =models.CharField(max_length=120)
    info= models.TextField()
    button =models.CharField(max_length=100,default="/log")
    teacher_name = models.CharField(max_length=200,null=True)
    rating = models.CharField(max_length=100,null=True)
    level = models.CharField(max_length=200,null=True)
    about_course = models.TextField(null=True)
    chapter1 = models.CharField(max_length=500,null=True)
    video1= models.FileField(upload_to='lecture_video/',null=True,blank=True)
    chapter2 = models.CharField(max_length=500,null=True)
    video2= models.FileField(upload_to='lecture_video/',null=True,blank=True)
    chapter3 = models.CharField(max_length=500,null=True)
    video3= models.FileField(upload_to='lecture_video/',null=True,blank=True)
    chapter4 = models.CharField(max_length=500,null=True)
    video4= models.FileField(upload_to='lecture_video/',null=True,blank=True)
    chapter5 = models.CharField(max_length=500,null=True)
    video5= models.FileField(upload_to='lecture_video/',null=True,blank=True)
    new_slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)
    # is_complete = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.product_name


# copy from youtube

# class course_info(models.Model):
#     main_id= models.ForeignKey()

class QuesModel(models.Model):
    sub = models.ForeignKey(course,on_delete=models.CASCADE)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.sub.product_name+"--"+ self.question


class completeCourse(models.Model):
    use = models.ForeignKey(User,on_delete=models.CASCADE)
    sub = models.ForeignKey(course,on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.use.first_name +""+self.sub.product_name

class sign_up_table (models.Model):
    main = models.OneToOneField(User,on_delete= models.CASCADE)
    mobile = models.IntegerField()
    profile_pic = models.ImageField(upload_to='profiles',null=True,blank=True,default="photo")
    add = models.CharField(max_length=500,null=True,blank=True)
    city_name = models.CharField(max_length=100,null=True,blank=True)
    state =models.CharField(max_length=50,null=True,blank=True)
    pincode = models.CharField(max_length=120, null=True,blank=True,default="0")
    p_mobile = models.CharField(max_length=15,null=True,blank=True)
    qualification = models.CharField(max_length=200,null=True,blank=True)
    update_date = models.DateTimeField(auto_now=True,null=True)
    collge_name = models.CharField(max_length=200,null=True,blank=True)
    about_me = models.TextField(null=True,blank=True)
    order_id = models.CharField(max_length=500,blank=True,null=True)
    amount = models.CharField(max_length=200,blank=True)
    razor_payemnt_id = models.CharField(max_length=500,blank=True)
    ispaid = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.main.username


 
class notification(models.Model):
    name = models.CharField(max_length=500,blank=True,null=True)
    main = models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name
    

class free_course(models.Model):
    core = models.ForeignKey(course,on_delete=models.CASCADE)
    theme = models.ImageField(upload_to="coursetheme",null=True, blank=True)
    youtube = models.CharField(max_length=500,null=True,blank=True)
    
    
    def __str__(self) -> str:
        return self.core.product_name
