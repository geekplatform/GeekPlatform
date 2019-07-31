from  django.urls import path
from  . import  views

app_name='challenge'

urlpatterns = [
    path(r'challenge/index',views.index,name='index'),
    #path(r'challenge/scoreboard',views.scoreboard,name='scoreboard'),
    path(r'challenge/info/<int:pk>',views.info,name="info"),
    path(r'challenge/scoreboard/<int:secret>/<int:category>/',views.scoreboard,name='scoreboard'),
    path(r'challenge/scoreboard/',views.rank,name='rank'),
    path(r'challenge/wrong',views.wrong,name='wrong'),
    path(r'challenge/success',views.success,name='success'),

]