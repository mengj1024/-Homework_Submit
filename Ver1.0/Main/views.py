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
                    return render(request,'老师-主页.html')
                else:
                    return render(request,"没有权限.html")

            else:
                 error_msg = "用户名或密码错误"
    return render(request, "registration/teacher-login.html", {"form_obj": form_obj, "error_msg": error_msg})

#老师登陆后进入老师主页
def TeacherHome(request):
    return render(request,'老师-主页.html')

#作业上传页面
def Taskupload_view(request):
    users = request.user
    stu=Student.objects.all()
    A=Student.objects.get(student_user=users)
    # B=A.abc_stu.count()
    # if B == 0:
    all_A=A.abc_stu.all()
    # print("A",all_A)
    # print(B)
    # print(users)
    return render(request,'Student/taskupload.html',{"grade":all_A})

#上传成功页面
def Taakupload_success(request):
    return render(request,'taskupload/upload_success.html')
    
#作业上传功能
from .models import Task,Student
def TaskUpload(request):
    users = request.user
    username = Student.objects.get(student_user=users)
    print(username)
    print(users)
    if request.method == 'POST':
        d= request.POST.get("grade1","") #上传者班级
        a=abc.objects.all()
        c=list()
        for b in a:
            if str(d)==str(b):
                e=Task.objects.filter(task_uploadname=username,task_grade=b).count()
                print(e)
                if e == 0:
                    myfile = request.FILES.get('file',None)
                    Image1 = Task(task_uploadname=username,task_upload=myfile,task_grade=b)
                    Image1.save()
                    return render(request,'taskupload/upload_success.html')
                else:
                    return render(request,"taskupload/upload_false.html")

#选项班级专业
def ChoiecsGradeMajor(request):
    return HttpResponse("2")

 #班级已选择
from .models import Grade
def ChoicedGrade(request):
    users = request.user
    username = Student.objects.get(student_user=users)
    print(username)
    if request.method == "POST":
        a=request.POST.get("grade","")
        print(a)
        b=abc.objects.get(abc_name=a)
        # print(b)
        c=Task.objects.filter(task_uploadname=username,task_grade=b)
        print(c)
        return render(request,'taskupload/班级已选择.html',{'grade':a,"task":c})
    else:
        return HttpResponse('2')

#学生头脑-查看作业
def student_e(request):
    users= request.user
    username= Student.objects.get(student_user=users)
    if request.method == "POST":
        b=request.POST.get("grade2","")
        img = request.POST.get("image","")
        c=abc.objects.get(abc_name=b)
        e=Task.objects.filter(task_grade=c,task_uploadname=username).count()
        if e==0:
            return render(request,"registration/还没上传过作业.html")
        # a=Task.objects.all()
        else:
            a=Task.objects.get(task_grade=c,task_uploadname=username)
            return render(request,"registration/查看作业.html",{"img":a,"img1":img})

def student_f(request):
    if request.method=="POST":
        name = request.POST.get("username","")
        grade = request.POST.get("usergrade","")
        grds  = request.POST.get("thumb","")
        print(grds)
        a1=request.POST.get("inlineRadioOptions","")
        comment1 = request.POST.get("comment","")
        b1=grade.strip()
        A1=Score.objects.get(score=a1)
        c1=abc.objects.get(abc_name=b1)
        e1=ID.objects.get(username=name)
        d1=Student.objects.get(student_user=e1)
        Task.objects.filter(task_grade=c1,task_uploadname=d1).update(task_score=A1,task_comment=comment1)

        img = request.POST.get("image","")
        # stuname = request.POST.get("stuname","")
        stugrade= request.POST.get("stu_grade","")
        # A=stugrade.strip()
        A=grade.strip()
        c=ID.objects.get(username=name)
        d=Student.objects.get(student_user=c)
        a=abc.objects.get(abc_name=A)
        Task.objects.filter(task_grade=a,task_uploadname=d).update(task_img=grds)
    return render(request,"Teacher/作业批改/发布成功.html")

#加入班级-选择专业
from .forms import Addgradeselectform,Selectmajorform
def add_major(request):
    if request.method == 'POST':
        b=Selectmajorform(request.POST)
        print(b)
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
from .models import abc
def add_grade_select(request):
    users = request.user
    if request.method == "POST":
        a=request.POST.get("major","")
        grades=abc.objects.filter(abc_id=a)
        for grade in grades:
            print(grade)
        print(grades)
        c=abc.objects.all()
        print(c)
        for d in c:
            print(d)
            if grade == d:
                # return HttpResponse("加入")
                b=Student.objects.get(student_user=users)
                print(b)
                b.abc_stu.add(d)
                return render(request,'Student/加入班级-选择成功.html')

#提交作业-选择班级
from .forms import submitselectgradeform,Teacherselectgradeform
def Submit_select_grade(request):
    users = request.user
    A=Student.objects.get(student_user=users)
    all_A=A.abc_stu.all()
    print("A",all_A)
    return render(request,'taskupload/选择班级.html', {'form':all_A})



#学生-头脑风暴
def Tou_1(request):

    return render(request,"Student/头脑风暴/1.html")


#老师-主页创建班级按钮
def creategrade(request):
    return render(request,"Teacher/创建班级.html")

#老师-创建班级名称
from .models import Teacher
def creategrade_name(request):
    users = request.user
    if request.method == "POST":
        a=request.POST.get("grade_name","")
        d=abc.objects.filter(abc_name=a).count()
        if d == 0:
            abc.objects.create(abc_name=a)   #创建班级
            c=abc.objects.get(abc_name=a)                      
            b=Teacher.objects.get(teacher_user=users)
            b.teacher_grade.add(c)
            return render(request,'Teacher/创建班级成功.html')  
        else:
            return HttpResponse("班级名已经存在")
   
#老师-作业批改
def task_check(request):
    users = request.user
    a=Teacher.objects.get(teacher_user=users)
    all_A=a.teacher_grade.all()
    post_list = a.teacher_grade.all()
    # print(post_list)
    return render(request,"Teacher/作业批改.html",{"grade":all_A,'post_list':a})


#老师选择班级
from .forms import Teacherselectgradeform
def teacher_sg(request):
    users = request.user
    a=Teacher.objects.get(teacher_user=users)
    A=a.teacher_grade.all()
    return render(request,"Teacher/作业批改1.html",{"teachergrade":A})


#老师头脑风暴选择班级
def teacher_e(request):
    users = request.user
    a=Teacher.objects.get(teacher_user=users)
    A=a.teacher_grade.all()
    return render(request,"Teacher/头脑风暴/Teacher-Tou_1.html",{"teachergrade":A})

#老师头脑风暴却定班级
def teacher_f(request):
    users = request.user
    username = Teacher.objects.get(teacher_user=users)
    if request.method == "POST":
        a=request.POST.get("grade","")
        aa=abc.objects.get(abc_name=a)
        print(a)
        c=Question.objects.filter(question_who=username,question_grade=aa)
        count=c.count()
        if count == 0:
            c=('无')
            b=('')
            A=Question.objects.filter(question_who=username)
            return render(request,"Teacher/头脑风暴/Teacher-Tou_3.html",{"grade":a,"answer":b,"question":c,"teacher_question":A})
        else:
            cc=Question.objects.get(question_who=username,question_grade=aa)
            b=Answer.objects.filter(question=cc)
            A=Question.objects.filter(question_who=username)
            print(A)     
            return render(request,"Teacher/头脑风暴/Teacher-Tou_3.html",{"grade":a,"answer":b,"question":c,"teacher_question":A})

#老师头脑风暴页面                         
def teacher_a(request):
    a=Answer.objects.all()
    b=Question.objects.all()
    return render(request,"Teacher/头脑风暴/Teacher-Tou.html",{"answers":a,"questions":b})

#老师头脑风暴提出问题
from .models import Question,Answer,ID
def teacher_b(request):
    users = request.user
    username = Teacher.objects.get(teacher_user=users)
    print(username)
    if request.method =="POST":
        grade = request.POST.get("grade","")
        Grade = abc.objects.get(abc_name=grade)
        print(Grade)
        count = Question.objects.filter(question_who=username).count()
        if count == 0:
            Questions = request.POST.get("Question","")
            a=Question.objects.create(question=Questions,question_who=username,question_grade=Grade)
            return render(request,"Teacher/头脑风暴/问题发布成功.html")
        else:
            return render(request,"Teacher/头脑风暴/问题发布失败.html")

def teacher_c(request):
    users = request.user
    username = ID.objects.get(username=users)
    username1 = Teacher.objects.get(teacher_user=users)
    if request.method =="POST":
        Answers = request.POST.get("Answer","")
        a=request.POST.get("grade2","")
        aa=abc.objects.get(abc_name=a)
        count = Answer.objects.filter(answer_who=username,answer_grade=aa).count()
        if count == 0:
            c=Question.objects.filter(question_who=username1,question_grade=aa)
            cc=Question.objects.get(question_who=username1,question_grade=aa)
            b=Answer.objects.create(answer=Answers,answer_who=username,question=cc,answer_grade=aa)
            return render(request,"Teacher/头脑风暴/回答发布成功.html")
        else:
            return render(request,"Teacher/头脑风暴/回答发布失败.html")


#删除当前问题
def teacher_d(request):
    users = request.user
    username = Teacher.objects.get(teacher_user=users)
    if request.method =="POST":
        Questions = Question.objects.all
        a=Question.objects.filter(question_who=username)
        A=a.delete()
        return render(request,"Teacher/头脑风暴/结束问题成功.html")


#提交作业选择班级确定
def teacherSub_s_1(request):
    if request.method ==  "POST":
        a=request.POST.get("grade","")  #获得当前选择班级
        aa=abc.objects.get(abc_name=a)  
        print(a)
        b=Task.objects.filter(task_grade=aa) #当前选择班级的学生
        return render(request,"Teacher/作业批改-确定班级.html",{"task":b})

#老师批改作业
def SBT(request):
    global img11
    if request.method=="POST":
        AbA=request.POST.get("username","")
        BaB=request.POST.get("usergrade","")
        B=BaB.strip()
        bb=abc.objects.get(abc_name=B)
        e=ID.objects.get(username=AbA)
        c=Student.objects.get(student_user=e)
        img11= Task.objects.filter(task_grade=bb,task_uploadname=c)
    return render(request,"Teacher/作业批改/作业批改页面.html",{"img11":img11,"username":AbA,"usergrade":BaB})

#作业批改页面
from .models import Score
def SBT2(request):
    if request.method =="POST":
        name = request.POST.get("username","")
        grade = request.POST.get("usergrade","")
        grds  = request.POST.get("thumb","")
        print(grds)
        a1=request.POST.get("inlineRadioOptions","")
        comment1 = request.POST.get("comment","")
        b1=grade.strip()
        A1=Score.objects.get(score=a1)
        c1=abc.objects.get(abc_name=b1)
        e1=ID.objects.get(username=name)
        d1=Student.objects.get(student_user=e1)
        Task.objects.filter(task_grade=c1,task_uploadname=d1).update(task_score=A1,task_comment=comment1)
    return render(request,"Teacher/作业批改/作业批改成功页面.html",{"img":grds,"username":name,"stugrade":grade})


def studnet_a(request):
    return render(request,"Student/头脑风暴/Tou-选择班级.html")

#学生头脑风暴-选择班级a
def student_b(request):
    users = request.user
    a=Student.objects.get(student_user=users)
    A=a.abc_stu.all()
    return render(request,"Student/头脑风暴/Tou-选择班级2.html",{"grade":A})

#学生头脑风暴-回答页面
def student_c(request):
    users = request.user
    username = Student.objects.get(student_user=users)
    if request.method == "POST":
        a=request.POST.get("grade","")
        aa=abc.objects.get(abc_name=a)
        c=Question.objects.filter(question_grade=aa)
        d=Question.objects.filter(question_grade=aa).count()
        print(d)
        if d == 0:
            return HttpResponse("此班级还没提出问题")
        else:
            cc=Question.objects.get(question_grade=aa)
            b=Answer.objects.filter(question=cc)
            return render(request,"Student/头脑风暴/Tou-选择班级3.html",{"grade":a,"question":c,"answer":b})

#学生头脑风暴-提交问题成功页面
def student_d(request):
    users = request.user
    username = ID.objects.get(username=users)
    if request.method =="POST":
        a=request.POST.get("answer","")
        grade= request.POST.get("grade","")
        print(grade)
        aa=abc.objects.get(abc_name=grade)
        print(aa)
        count = Answer.objects.filter(answer_who=username).count()
        print(count)
        if count == 0:
            c=Question.objects.filter(question_grade=aa)
            cc=Question.objects.get(question_grade=aa)
            b=Answer.objects.create(answer=a,answer_who=username,question=cc)
            return render(request,"Student/头脑风暴/Tou-提交成功.html")
        else:
            return render(request,"Student/头脑风暴/Tou-提交失败.html")