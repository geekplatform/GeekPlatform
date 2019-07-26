from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import TeamFormsDIY, TeamChangeForms
from django.contrib.auth.decorators import login_required
from .models import Teams
# Create your views here.

def index(request):
    content = {}
    if request.user:
        content['team'] = request.user
    return render(request,'accounts/index.html',content)

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
        #register_form = TeamFormsDIY(request.POST)
        register_form = UserCreationForm(request.POST)
        # 判断表单是否填写正确
        if register_form.is_valid():
            # 正确就保存
            register_form.save()
            # 用保存的表单数据创建新用户
            new_team = authenticate(username=register_form.cleaned_data['username'],password=register_form.cleaned_data['password1'])
            Teams(team=new_team).save()
            # 注册完成，保持用户登录
            auth_login(request,new_team)
            # 重定向到主页
            return redirect('accounts:index')
    # 不是POST请求得到填写表单
    else:        
        register_form = UserCreationForm()
        #register_form = TeamFormsDIY(request.POST)
    # 将填写表单赋值到字典
    content['register_form'] = register_form
    # 返回注册界面
    return render(request,'accounts/register.html',content)

# 必须为登录才能加载页面，否在跳转到登录页面
@login_required(login_url='accounts:login')
# 队伍信息页面
def team_information(request):
    content = {}
    # 队伍已登录，直接获取登录用户信息。
    content['team_information'] = request.user
    # 传到模板
    return render(request, 'accounts/team_information.html',content)

# 必须为登录才能加载页面，否在跳转到登录页面
@login_required(login_url='accounts:login')
def change_information(request):
    content = {}
    # 如果为POST请求
    if request.method == 'POST':
        # 获得自定意义表单
        change_information_forms = TeamChangeForms(request.POST,instance=request.user)
        # 判断填写信息是否符合要求
        if change_information_forms.is_valid():
            # 保存表单信息
            change_information_forms.save()
            # 以下在在给表赋值
            request.user.teams.team_member_one_name = change_information_forms.cleaned_data['member_one_name']
            request.user.teams.team_member_two_name = change_information_forms.cleaned_data['member_two_name']
            request.user.teams.is_school = change_information_forms.cleaned_data['is_school']
            request.user.teams.is_freshman = change_information_forms.cleaned_data['is_freshman']
            request.user.teams.team_member_one_school_ID = change_information_forms.cleaned_data['member_one_school_ID']
            request.user.teams.team_member_two_school_ID = change_information_forms.cleaned_data['member_two_school_ID']
            # 保存用户表
            request.user.teams.save()
    else:
        # 不是POST请求，就新建一个表单
        change_information_forms = TeamChangeForms(instance=request.user)
    # 把表单传到模板
    content['change_information_forms'] = change_information_forms
    # 用户信息传到模板，是为了默认填写
    content['team_information'] = request.user
    return render(request, 'accounts/team_information.html',content)

# 必须为登录才能加载页面，否在跳转到登录页面
@login_required(login_url='accounts:login')
# 修改密码
def change_password(request):
    content = {}
    # 如果为POST请求
    if request.method == 'POST':
        # 用django自带的修改密码表单，得到用户填写新密码
        change_password_forms = PasswordChangeForm(data=request.POST, user=request.user)
        # 如果用户填写符合要求
        if change_password_forms.is_valid():
            # 保存修改后的密码
            change_password_forms.save()
            # 跳转到登录界面
            return redirect('accounts:login')
    else:
        # 不是POST请求，直接返回修改密码表单
        change_password_forms = PasswordChangeForm(user=request.user)

    content['change_password_forms'] = change_password_forms
    content['team'] = request.user
    return render(request, 'accounts/change_password.html',content)
