from . import views
from django.urls import path

app_name = 'notice'
urlpatterns = [
    path('notice', views.index, name='index'),

]
