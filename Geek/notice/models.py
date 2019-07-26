from django.db import models


# 公告
class Notice(models.Model):
    # 标题
    title = models.CharField(max_length=200, verbose_name="公告题目")
    # 内容
    content = models.TextField(verbose_name="公告内容")
    # 时间
    created_time = models.DateTimeField(verbose_name="公告时间")
