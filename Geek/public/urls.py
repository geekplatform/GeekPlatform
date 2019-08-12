from  django.urls import path
from  . import  views

app_name='public'

urlpatterns = [
    path(r'public/about',views.about,name='about'),
    path(r'public/notifications',views.notifications,name='notifications'),
    

]