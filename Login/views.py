
# Create your views here.
from django.shortcuts import render, redirect,render_to_response
from .forms import RegisterForm
from django.http import HttpResponse


def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST,request.FILES)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})


def home(request):
    a=Student.objects.all()
    return render(request, 'home/home.html',{"stu":a})

# def login(request):
#     return render(request,'users/login.html')
from django.template import Context, Template
from .models import ImageUpload

def upload(request):
    users = request.user.username
    if request.method == 'POST':
        # stu_home = request.POST.get("上传者","")
        # ImageUpload.objects.filter(students_home=stu_home)
        # c=str(stu_home)
        # a=ImageUpload()
        # a.students_home=c
        # a.save()
        Image1 = ImageUpload.objects.all()
        b=list()
        for ob in Image1:
            a=ob.upload_name
            b.append(a)
        # print(b)
        c=b.count(request.user.username)
        # print(c)

            # for i in b:
            #     if b.count
        # for users in Image1.users:
        #     print(users)
        # get(upload_name=users,default=None)
        if c == 0:
            myfile = request.FILES.get('file',None)
            # with open('media/%s'%myfile,'wb') as fn:
            #     fn.write(myfile.read())
            # #     file_name = print(fn.name)
            # #     # upload_name = print(fn)
            # #     fn.write(myfile.read())
            # #     fn.close()
            # a=myfile.name
            Image1 = ImageUpload(name=myfile.name,upload_name=users,img=myfile)
            Image1.save()
            return render(request,'files_upload/upload_success.html')
        else:
            return HttpResponse("已经上传过作业")
    else:
        return HttpResponse("erroe")

from .models import ImageUpload,User,Chengji,Student
def delete(request):
    users = request.user
    if request.method == 'POST':
        Image2 = ImageUpload.objects.get(upload_name=users)
        Image2.delete()
        return HttpResponse("删除成功")

    else:
        return HttpResponse("删除失败")




def Students_message(request):
    users = request.user
    homework = ImageUpload.objects.all()
    stu      = Student.objects.all()   
    print(users)
    return render(request,'Teachers/学生信息.html',{'user':users,'homework':homework,'stu':stu})

def Homework_ck(request):
#    users =
    user = Student.objects.all()
#    print(user)
    homework = ImageUpload.objects.all()
    b=list()
    c=list()
    # imgs = ImageUpload.objects.all()
    for a in user:
    #     print(a)
    #     c.append(a)
    # print(c)
    # d= c[8:]
    # print(d)
    # for f in d:
    #     print(f)
        usera = Student.objects.get(nickname=a)
    #        print(usera)
        # imgs =  ImageUpload.objects.get(upload_name=f)
        # b.append(imgs)
#    print(b)
#        print(cheak)
#    print(users)
#    print(user)
    return render(request,"Teachers/作业批改.html",{'stu':user,'img':b,'homework':homework})

def test3(request):
    username = request.POST.get("查看","")
    # print("username",username,type(username))
    user = Student.objects.all()
    # print(type(user))
    for c in user:
        d=c.students_name
        g=str(d)
        if g == username:
            AA=d
    # print(AA)
    # print(type(AA))
    # print(type(g))
    # print(c)
    b=list()
    c=list()
    # imgs = ImageUpload.objects.all()
    # for a in user:
    imgs =  ImageUpload.objects.all()
    # print(imgs)
    for B in imgs:
        c.append(B)
        C=str(B)
        # print("B",B)
        b.append(C)
    # print("b",b,"c",c)
    # print("C",C,type(C))
    if username in b:
        Q=b.index(username)
        # print(Q)
        D=c[Q]
    # print(type(D))    
        return render(request,"registration/2333.html",{'stu':user,'img':D,'ss':AA,'aa':username})
    else:
        return HttpResponse("2333")
    # return HttpResponse('233')
    # return render(request,"registration/2333.html",{'stu':user,'img':imgs,'ss':AA,'aa':username})
    # print(type(BB))
    

def Tou(request):
    return render(request,"Teachers/头脑风暴.html")

def teacher_home(request):
    return render(request,"Teachers/首页.html")

def Login_teacher(request):
  return render(request,"Teachers/login.html")

from .forms import TeacherloginForm
from django.contrib import auth

def teacherlogin(request):
    error_msg = ""
    form_obj = TeacherloginForm()
    if request.method == "POST":
        form_obj = TeacherloginForm(request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data.get("username")
            password = form_obj.cleaned_data.get("password")
            # if username == "Q1mi" and password == "123456":
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if user.is_staff:
                    return render(request,'Teachers/首页.html')
                else:
                    return HttpResponse("没有权限")    

            else:
                 error_msg = "用户名或密码错误"
    return render(request, "registration/teacher-login.html", {"form_obj": form_obj, "error_msg": error_msg})

def message(request):
    users = request.user
    user = User.objects.all()
    homework = ImageUpload.objects.all()
    # chengji = Student.objects.get(students_name=users)
    print(users)

    return render(request,"home/message.html",{'users':user,'homework':homework,})
    
def chengji_cheak(request): 
    users = request.user
    chengji = Student.objects.get(students_name=users)

    return render(request,"home/changji_cheak.html",{'chengji':chengji})



def image(request):
    # response = HttpResponse(open('media/%s'%filename,'rb').read())
    # response["content-Type"] = 'image/jpeg'
    # return response
    users = request.user.username
    imgs =  ImageUpload.objects.get(upload_name=users)
    # user = User.objects.all()
    # print(imgs)
    # print(users)
    # print(user) 
    homework = ImageUpload.objects.all()
    return render(request,"registration/Welcome.html",{"img":imgs,'homework':homework})


# from .models import Comment
# from django.contrib.contenttypes.models import ContentType
# def upload_comment(request):
#     return render(request,"TOU/Tou.html")

from .models import Questions,Answers
def Test(request):
    # if request.method =='POST':
    #     Q1 = request.POST.get('text','')
    #     Q2 = Questions(Question=Q1)
    #     Q2.save()
    #     print(Q1)
        users = User.objects.all()
        Answers_name = Answers.objects.all()
        # b=Answers_name.values_list('Answer')
        # Answer      = Answers.objects.all().values()
        Question     = Questions.objects.get()
        # print(Answers_name)
        # # print(b)
        print(Question)
        return render(request,"home/Tou.html",{'answer':Answers_name,'Question':Question},)
    # else:
    #     return HttpResponse('2333')


def Test2(request):
    users = request.user
    chengji = Student.objects.get(students_name=users)
    return render(request,"home/changji_cheak.html",{'chengji':chengji})

def comments(request):
    user = request.user
    if request.method =='POST':
        Q1 = request.POST.get('text',None)
        Q2 = Answers(Answer=Q1,Answer_name=user)
        Q2.save()
        return HttpResponse("1")
    else:
        return HttpResponse("233")

from .forms import PiGaiForm
def pigai(request):
    username =request.POST.get("username1","")
    print(username)
    a= PiGaiForm()
    if request.method == "POST":
        a = PiGaiForm(request.POST)
        # print(a)
        return render(request,"registration/2444.html",{'a':a,'username2':username})
    else:
        return HttpResponse("2")
    
    return render(request,"registration/2444.html",{'a':a,'username2':username})

def pigai1(request):
    from Login import forms
#    from django.forms import fields,widgets
#    a = forms.PiGaiForm()
#    b=a.fields['grade'].choices
#    print(b)
#    return HttpResponse('233')
    
    if request.method=='POST':
        W = request.POST.get("学生姓名","")
        # print(username)
        username=W.strip()
        # a=PiGaiForm(request.POST)
        # b=Chengji.objects.all()
        # c=ImageUpload.objects.get(hw_chengji=Q1)
        # print(a)
        # print("b=",b)
        Q1 = request.POST.get('test',None)
        # print(a)
        # c=ImageUpload.objects.get(hw_chengji=Q1)
        print("对应成绩id=",Q1)
        d=Chengji.objects.get(pk=Q1) #包含成绩的ID
        c=ImageUpload.objects.all()
        # .values_list("upload_name")
        for aa in c:
            bb=str(aa)
            # print(type(bb))
            # print(bb)
            # print(username)
            # print(type(username))
            if username == bb:
                B=ImageUpload.objects.filter(upload_name=aa).update(hw_chengji=d) #包含学生的ID
                print(B)
                break
            else:
                print("2")
        print("成绩=",d)
        # print(c)
        # c=ImageUpload.objects.all().values_list("upload_name")
        # d=Chengji.objects.get(pk=Q1)
        # print(c)
        # print(d)
        # f =ImageUpload()

        # f.save()
        return HttpResponse('2333')
    else:
        return HttpResponse('2')

