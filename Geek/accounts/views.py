from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):

    return render(request,'accounts/index.html')

# 登录逻辑
def login(request):

    # 如果为POST请求
    if request.method == 'POST':
        # 验证用户密码
        team = authenticate(request,username=request.POST['teamname'],password=request.POST['password'])
        # 如果返回为none，帐号或密码错误，或用户不存在
        if team is None:
            # 携带错误提示重定向到登录页面
            return render(request,'accounts/login.html',{'error':'用户bu存在'})
        # 验证成功，保持登录，并重定向到主页
        else:
            # 保持登录状态
            auth_login(request,team)
            # 重定向到主页
            return redirect('accounts:index')
    # 如果为GET请求
    else:
        # 返回登录界面
        return render(request,'accounts/login.html')

# 登出逻辑
def logout(request):
    # 直接登出
    auth_logout(request)
    # 重定向到主页
    return redirect('accounts:index')


# 注册逻辑
def register(request):
    # 创建一个空字典，为下面传到模板中使用
    content = {}
    # 如果为POST请求，验证表中信息
    if request.method == 'POST':
        # Django自带表单获取帐号密码
        register_form = UserCreationForm(request.POST)
        # 判断表单是否填写正确
        if register_form.is_valid():
            # 正确就保存
            register_form.save()
            # 用保存的表单数据创建新用户
            new_team = authenticate(username=register_form.cleaned_data['username'],password=register_form.cleaned_data['password1'])
            # 注册完成，保持用户登录
            auth_login(request,new_team)
            # 重定向到主页
            return redirect('accounts:index')
    # 不是POST请求得到填写表单
    else:        
        register_form = UserCreationForm()
    # 将填写表单赋值到字典
    content['register_form'] = register_form
    # 返回注册界面
    return render(request,'accounts/register.html',content)