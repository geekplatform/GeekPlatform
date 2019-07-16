from django.shortcuts import render,redirect
from .models import Challenge
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    challenge_list=Challenge.objects.all().order_by('-created_time')
    return render(request,'test.html',context={'challenge_list':challenge_list})
