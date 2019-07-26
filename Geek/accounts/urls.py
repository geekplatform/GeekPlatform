from django.urls import path,include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('accounts/login/',views.login,name='login'),
    path('accounts/logout',views.logout,name='logout'),
    path('accounts/register',views.register,name='register'),
    path('accounts/change_information',views.change_information,name='change_information'),
    path('accounts/change_password',views.change_password,name='change_password'),
    path('',views.index,name='index'),
]