from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.

# 通知表
class Notice(models.Model):
    # 内容
    content = models.TextField(verbose_name="正文",blank=True,null=True)
    # 创建时间
    Create_time =  models.DateTimeField(verbose_name="创建时间")

    def __str__(self):
        return self.Create_time


class Introduce(models.Model):
    # 标题
    title = models.CharField(max_length=50, default="", verbose_name="题目")
    # 内容
    content = MDTextField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
