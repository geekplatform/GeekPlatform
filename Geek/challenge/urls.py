from  django.urls import path,include
from  . import  views
app_name='challenge'

urlpatterns = [
    path(r'challenge/index',views.index,name='index'),
    path(r'challenge/scoreboard',views.scoreboard,name='scoreboard'),
<<<<<<< HEAD
    path(r'challenge/info/<int:pk>',views.info,name="info"),
=======
>>>>>>> bd81a28ca904d29ed5af335e7a292a2877a0a316
    ]