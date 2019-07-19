"""
在Django自带表单基础上，自定义表单，继承原来的表单
TeamFormsDIY为创建用户表单，注册用户时需要的填写的信息，不过我没使用
TeamChangeForms为用户修改信息表单，修改信息时可用
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

# 自定义表单
class TeamFormsDIY(UserCreationForm):
    # 队员一名字
    member_one_name = forms.CharField(required=True, max_length=50, label='队员一ID')
    # 队员二名字
    member_two_name = forms.CharField(required=True, max_length=50, label='队员二ID')
    # 队伍时否为本校队伍
    is_school = forms.NullBooleanField(required=True, label='是否为本校学生')
    # 队员一学号
    member_one_school_ID = forms.CharField(required=True, max_length=50, label='队员一学号')
    # 队员二学号
    member_two_school_ID = forms.CharField(required=True, max_length=50, label='队员二学号')

    class Meta:
        # 属于User 
        model = User
        # 定义普通用户可修改字段
        fields = ['username',]


class TeamChangeForms(UserChangeForm):
    member_one_name = forms.CharField(required=True, max_length=50, label='队员一ID')
    # 队员二名字
    member_two_name = forms.CharField(required=True, max_length=50, label='队员二ID')
    # 队伍时否为本校队伍
    is_school = forms.NullBooleanField(required=True, label='是否为本校学生')
    # 队员一学号
    member_one_school_ID = forms.CharField(required=True, max_length=50, label='队员一学号')
    # 队员二学号
    member_two_school_ID = forms.CharField(required=True, max_length=50, label='队员二学号')

    class Meta:
        # 属于User 
        model = User
        # 定义普通用户可修改字段
        fields = ['username','member_one_name','member_two_name','is_school','member_one_school_ID','member_two_school_ID']