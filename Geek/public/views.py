from django.shortcuts import render
from .models import Introduce, Notice

# Create your views here.

def about(request):

    introduce = Introduce.objects.first()
    
    context = { 'introduce': introduce }
    
    return render(request, 'about.html', context)


def notifications(request):

    notice = Notice.objects.all().order_by('-Create_time')

    context = { 'notifications': notice }

    return render(request, 'notifications.html', context)

