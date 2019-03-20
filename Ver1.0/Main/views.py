from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect,render_to_response
from .forms import registerform
from django.http import HttpResponse

# 注册views
def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = registerform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = registerform()
    return render(request, 'user/register.html', context={'form': form, 'next': redirect_to})

def home(request):
    return render(request,'主页.html')

#老师登陆
from .forms import TeacherLoginform
from django.contrib import auth
def TeacherLogin(request):
    error_msg = ""
    form_obj = TeacherLoginform()
    if request.method == "POST":
        form_obj = TeacherLoginform(request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data.get("username")
            password = form_obj.cleaned_data.get("password")
            # if username == "Q1mi" and password == "123456":
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if user.is_staff:
                    return render(request,'老师-首页.html')
                else:
                    return HttpResponse("没有权限")    

            else:
                 error_msg = "用户名或密码错误"
    return render(request, "registration/teacher-login.html", {"form_obj": form_obj, "error_msg": error_msg})

#老师登陆后进入老师主页
def TeacherHome(request):
    return render(request,'老师-主页.html')

#作业上传页面
def Taskupload_view(request):
    users = request.user.username
    stu=Student.objects.all()
    print(users)
    return render(request,'Student/taskupload.html')

#上传成功页面
def Taakupload_success(request):
    return render(request,'taskupload/upload_success.html')
    
#作业上传功能
from .models import Task,Student
def TaskUpload(request):
    users = request.user.username
    print(users)
    if request.method == 'POST':
        d= request.POST.get("grade1","")
        Image1 = Task.objects.all()
        b=list()
        for ob in Image1:
            a=ob.task_uploadname
            b.append(a)
        c=b.count(request.user.username)
        grades=Task.objects.all()
        D=list()
        for oa in grades:
            E=oa.task_grade
            e=str(E)
            D.append(e)
        print(D)
        print(d)
        F = D.count(d)
        d= request.POST.get("grade1","")
        e= Grade.objects.all()
        for A in e:
            B=str(A)
            C=str(d)
            print(B)
            print(C)
            if B == C:
                # return HttpResponse('2333')
                if c != 0 and F >= 1: 
                    # myfile = request.FILES.get('file',None)
                    # Image1 = Task(task_uploadname=users,task_upload=myfile,task_grade=A)
                    # Image1.save()
                    # return render(request,'taskupload/upload_success.html')
                    return HttpResponse("已经上传过作业")
                    # return HttpResponse('2333')
                else:
                    myfile = request.FILES.get('file',None)
                    Image1 = Task(task_uploadname=users,task_upload=myfile,task_grade=A)
                    Image1.save()
                    return render(request,'taskupload/upload_success.html')
                    
            # else:
    return HttpResponse("2")

        
        
       
#选项班级专业
def ChoiecsGradeMajor(request):
    # if request.method == "POST":
    #     # a=Grademajorform(request.POST)
    #     b=Gradenameform(request.POST)
    #     # print(a)
    #     print(b)
    #     ,{'gradename':b})
    # else:
    return HttpResponse("2")

 #班级已选择
from .models import Grade
def ChoicedGrade(request):
    if request.method == "POST":
        a=request.POST.get("grade","")
        print(a)
        b=Grade.objects.get(grade_id=a)
        print(b)
        return render(request,'taskupload/班级已选择.html',{'grade':b})
    else:
        return HttpResponse('2')

#加入班级-选择专业
from .forms import Addgradeselectform,Selectmajorform
def add_major(request):
    if request.method == 'POST':
        b=Selectmajorform(request.POST)
        
        # print(a)
        return render(request,'Student/加入班级-加入专业.html',{'major':b})
    
#加入班级-选择班级
def add_grade(request):
    if request.method == 'POST':
        a=Addgradeselectform(request.POST)
        b= request.POST.get('major',"")
        print(b)
        c=Grade.objects.filter(grade_major=b)
        print(c)
        return render(request,'Student/加入班级-加入班级.html',{'grade':c})

#加入班级-选择班级专业
def add_grade_select(request):
    users = request.user
    if request.method == "POST":
        a=request.POST.get("grade","")
        B=request.POST.get('add_major',"")
        C=request.POST.get('add_grade',"")
        A=a.strip()
        print(A)
        print(B)
        print(C)
        c=Grade.objects.all()
        for d in c:
            if str(d) == A:

                b=Student.objects.get(student_user=users)
                b.student_grade.add(d)
                return render(request,'Student/加入班级-选择成功.html')
    # return render(request,'Student/加入班级-选择成功.html')
    # return HttpResponse("加入'''")
        # print(users)
        # print(a)
        # c=Grade.objects.get(grade_id=a)
        # print(c)
        # b=Student.objects.filter(student_user=users).update(student_grade=c)
        # print(b)
        

#提交作业-选择班级
from .forms import submitselectgradeform
def Submit_select_grade(request):
    users = request.user
    a=Student.objects.all()
    for A in a :
        print(A)
        print(str(A))
        if str(users) == str(A):
            b=Grade.objects.filter(stu_name=A)
            c=Grade.objects.get(stu_name=A)
            print(c)
            print(b)
            return HttpResponse('1')
        else:
            return HttpResponse("2")
    # form = submitselectgradeform()
    # if request.method == "POST":
    #     form = submitselectgradeform(request.POST)
    #     return render(request,'taskupload/选择班级.html', {'form':form})
    # else:
    # return HttpResponse('233')