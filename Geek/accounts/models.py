from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 团队数据库
class Teams(models.Model):
    # 团队数据库名字一对一User
    team = models.OneToOneField(User, on_delete=models.CASCADE)
    # 队员一名字
    team_member_one_name = models.CharField(blank=True, null=True, max_length=50)
    # 队员二名字
    team_member_two_name = models.CharField(blank=True, null=True, max_length=50)
    # 队伍时否为本校队伍
    is_school = models.NullBooleanField()
    # 队员一学号
    team_member_one_school_ID = models.CharField(blank=True, null=True, max_length=50)
    # 队员二学号
    team_member_two_school_ID = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        verbose_name_plural = "Teams"

