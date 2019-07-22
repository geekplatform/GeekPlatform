from . import views
from django.urls import path

app_name = 'notice'
urlpatterns = [
    path('', views.index, name='index'),
]
