from django.contrib import admin

# Register your models here.
from .models import Notice


class NoticeAdd(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_time']
admin.site.register(Notice, NoticeAdd)