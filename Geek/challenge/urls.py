from  django.urls import path,include
from  . import  views
app_name='challenge'

urlpatterns = [
    path(r'challenge/index',views.index,name='index'),
    path(r'challenge/scoreboard',views.scoreboard,name='scoreboard'),
    ]