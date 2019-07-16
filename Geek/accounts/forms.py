from django.contrib.auth.forms import UserCreationForm
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