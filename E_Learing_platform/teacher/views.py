from django.shortcuts import render , redirect
from django.contrib.auth import logout
from home.models import sign_up_table,notification
from django.contrib.auth.models import User
from student.models import quires
from teacher.models import qanswers , assignment,lecture,notes
from home.models import course
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def index1(request):
    questions = qanswers.objects.all()
    noti = notification.objects.all()
    assignmentcount = assignment.objects.all().count()
    notescount = notes.objects.all().count()
    leccount = lecture.objects.all().count()
    qcount = quires.objects.all().count()
    quir = quires.objects.all()
    pending = quires.objects.exclude(id__in=questions.values('ques_id')).count()
    pending_data = quires.objects.exclude(id__in=questions.values('ques_id'))
    data ={
        "noti":noti,
        "assignmentcount":assignmentcount,
        "notescount":notescount,
        "leccount":leccount,
        "qcount":qcount,
        "quir":quir,
        "pending":pending,
        "pending_data":pending_data
    }
    return render(request,"teacher/teacher_dashboard.html",data)

def assignment1(request):
    sub = course.objects.all()
    note = notes.objects.all()
    lec = lecture.objects.all()
    assign =assignment.objects.all()
    data = {
        "sub":sub,
        "note":note,
        "lec":lec,
        "assign":assign
    }
    
    return render(request,"teacher/teacher_assignment.html",data)

def addlecture(request):
    sub = course.objects.all()
    data = {
        "sub":sub
    }
    if request.method == "POST":
        print(request.POST)
        lecture_id = request.POST.get('sub')
        try:
            lecture_sub = course.objects.get(product_name=lecture_id)
            link = request.POST.get('link')
            time = request.POST.get('time')
            chapter = request.POST.get('chapter')
            lecture.objects.create(
                subject=lecture_sub,
                link=link,
                time=time,
                chapter=chapter
            )
            return redirect('teacherassignment')
        except lecture.DoesNotExist:
            # Handle the case when no course is found
            data["error"] = f"Course '{lecture_id}' not found."
        except Exception as e:
            # Handle any other exceptions
            data["error"] = str(e)
    
    return render(request,"teacher/add_lecture.html",data )

def addassignment(request):
    sub = course.objects.all()
    data = {
        "sub":sub
    }
    if request.method == "POST":
        print(request.POST)
        assignment_id = request.POST.get('ass-sub')
        print(assignment_id)
        try:
            assignment_sub = course.objects.get(product_name=assignment_id)
            ass_name = request.POST.get('ass-name')
            file = request.FILES.get('file')
            assignment.objects.create(
                subject=assignment_sub,
                assignment_name=ass_name,
                assignment_file=file
            )
            data["success"] = "Assignment added successfully."
            return redirect('teacherassignment')
        except course.DoesNotExist:
            data["error"] = f"Course '{assignment_id}' not found."
        except Exception as e:
            data["error"] = str(e)
    return render(request, "teacher/add_assignment.html", data)




def addnotes(request):
    sub = course.objects.all()
    data = {
        "sub":sub
    }
    if request.method == "POST":
        print(request.POST)
        notes_id = request.POST.get('notes-sub')
        print(notes_id)
        try:
            notes_sub = course.objects.get(product_name=notes_id)
            notes_name = request.POST.get('notes-name')
            notesfile = request.FILES.get('notesfile')
            notes.objects.create(
                subject=notes_sub,
                notes_name=notes_name,
                notes_file=notesfile
            )
            data["success"] = "Assignment added successfully."
            return redirect('teacherassignment')
        except course.DoesNotExist:
            data["error"] = f"Course '{notes_id}' not found."
        except Exception as e:
            data["error"] = str(e)
    return render(request,"teacher/add_notes.html" ,data)

def chat(request):
    ans = quires.objects.all()
    questions = qanswers.objects.all()
    
    if request.method == "POST":
        question_id = request.POST.get('question')
        ques = quires.objects.get(Question=question_id)
        answer = request.POST.get('ans')
        img = request.FILES.get('ans_file')
        
        # Create a new qanswers instance
        qanswers.objects.create(
            ques=ques,
            answer=answer,
            a_img=img
        )
    # pending =[]
    # for i in questions :
    #     temp = quires.objects.filter(id =i.ques.id)
    #     pending.extend(temp)

    # print(pending)
    # pending = ans.exclude(id=questions.values('ques_id'))
    pending = quires.objects.exclude(id__in=questions.values('ques_id'))
    # print(pending)
        
    data = {"ans": ans, "questions": questions,"pending":pending }
    return render(request, "teacher/teacher_chat.html", data)


def profile(request):
    context ={}
    data = sign_up_table.objects.get(main__id=request.user.id)
    # print(data)
    context["data"]=data
    if request.method == "POST":
        print(request.POST)
        # print(request.file)
        profile_pic = request.POST.get('profile-photo')
        email= request.POST.get('Email')
        frist_name= request.POST.get('Frist_Name')
        last_name = request.POST.get('Last_Name')
        add = request.POST.get('Address')
        city = request.POST.get('City')
        state = request.POST.get('State')
        pincode = request.POST.get('Pincode')
        about_me = request.POST.get('aboutme')
        mo=request.POST.get('no')
        parent_no = request.POST.get('p_no')
        qualification = request.POST.get('Qualification')
        college = request.POST.get('College')

        urs = User.objects.get(id=request.user.id)
        urs.first_name=frist_name
        urs.last_name=last_name
        urs.email=email
        urs.save()

        data.mobile=mo
        data.add = add
        data.city_name =city
        data.state = state
        data.pincode =pincode
        data.about_me=about_me
        data.p_mobile =parent_no
        data.qualification =qualification
        data.collge_name =college
        data.save()

        if "profile-photo" in request.FILES :
            img = request.FILES["profile-photo"]
            data.profile_pic =img
            data.save()

        context["status"]= "Changes save Successfully "
    return render(request,"teacher/teacher_profile.html",context)



def student_logout(request):
    logout(request)
    return render(request,"login.html")
    # return HttpResponse("back to home")



@login_required
def changepassword(request):
    if request.method =="POST":
        # print(request.POST)
        username = request.POST.get('username')
        oldpassword = request.POST.get('oldpassword')
        newpassword  = request.POST.get('newpassword')  
        # keyuser = authenticate(request,username=username,password=oldpassword)
        # main = User.objects.get(id=request.user.id)
        # print(keyuser)
        # print(main)
        # if keyuser is not None:
        #     main.set_password(newpassword)
        #     main.save()
        #     return redirect('dashboard')

        if not check_password(oldpassword, request.user.password):
            return render(request, "password.html", {"error": "Old password is incorrect"})

        request.user.set_password(newpassword)
        request.user.save()
        update_session_auth_hash(request, request.user)

        return redirect('teacherdashboard')

    return render(request,"password.html")