from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#分类
class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="分类")

    def __str__(self): return self.name
class Author(models.Model):
    name=models.CharField(max_length=20,verbose_name="出题人")

    def __str__(self): return self.name
#题目
class Challenge(models.Model):
    #题目
    title = models.CharField(max_length=200,blank=True, null=True,verbose_name="题目")
    #正文
    text=models.TextField(verbose_name="正文")
    #创建时间
    created_time = models.DateTimeField(verbose_name="创建时间")
    #最后一次修改时间
    modified_time = models.DateTimeField(verbose_name="最后一次修改时间")
    #作者
    author=models.ForeignKey(Author,verbose_name="出题人",on_delete=models.CASCADE)
    #提示
    hints=models.TextField(verbose_name="提示",blank=True)
    #分类
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="类型")
    #flag
    flag=models.TextField(verbose_name="flag")
