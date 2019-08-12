from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# 分类
class Category(models.Model):
    # 分类的名字
    name = models.CharField(max_length=20, verbose_name="分类")

    def __str__(self): return self.name


class Author(models.Model):
    # 出提人头像
    header_img = models.ImageField(verbose_name='出题人头像')
    # 出题人
    name = models.CharField(max_length=20, verbose_name="出题人")
    # 出题人QQ
    QQ = models.TextField(blank=True, null=True)

    def __str__(self): return self.name


class Challenge(models.Model):
    # 题目
    title = models.CharField(max_length=200, default="", verbose_name="题目")
    # 正文
    content = models.TextField(verbose_name="正文")
    # 题目地址
    link = models.CharField(verbose_name="题目地址",null=True,max_length=500,default=" ")
    # 创建时间
    created_time = models.DateTimeField(verbose_name="创建时间")
    # 最后一次修改时间
    modified_time = models.DateTimeField(verbose_name="最后一次修改时间")
    # 作者
    author = models.ForeignKey(Author, verbose_name="出题人", on_delete=models.CASCADE)
    # 提示
    hints = models.TextField(verbose_name="提示", blank=True)
    # 分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="类型")
    # flag
    flag = models.CharField(max_length=30, blank=False, default="")
    # 是否隐藏
    state = models.IntegerField(choices=[(0, 'hidden'), (1, 'obvious')], default=0, verbose_name="是否隐藏")
    # 分数
    value = models.PositiveIntegerField(default=0, verbose_name="分数")

    def __str__(self): return self.title


class Solve(models.Model):
    # 这个题的id
    challenge_id = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name="s_challenge_id")
    # 谁解决了这个问题
    team_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_id")
    # 提交flag时间
    created_time = models.DateTimeField(auto_now_add=True)
