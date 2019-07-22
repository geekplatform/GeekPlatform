from django.contrib import admin

# Register your models here.
from .models import Notice


class NoticeAdd(admin.ModelAdmin):
    list_display = ['Notice_name', 'Notice_text', 'pub_date']
admin.site.register(Notice, NoticeAdd)