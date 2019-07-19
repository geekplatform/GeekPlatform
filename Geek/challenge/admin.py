from django.contrib import admin
from .models import Category,Challenge,Author
# Register your models here.
class ChallengeAdd(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
admin.site.register(Challenge, ChallengeAdd)
admin.site.register(Category)
admin.site.register(Author)
