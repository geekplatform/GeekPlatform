from django.db import models


# 公告
class Notice(models.Model):
    # 标题
    Notice_name = models.CharField(max_length=200, verbose_name="公告题目")
    # 内容
    Notice_text = models.CharField(max_length=1000, verbose_name="公告内容")
    # 时间
    pub_date = models.DateTimeField(verbose_name="公告时间")
