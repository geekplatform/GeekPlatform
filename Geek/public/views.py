from django.shortcuts import render
from .models import Introduce, Notice
import markdown
# Create your views here.

def about(request):

    introduce = Introduce.objects.first()
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ])

    if introduce:
        introduce.content = md.convert(introduce.content)

    context = { 'introduce': introduce }
    
    return render(request, 'about.html', context)


def notifications(request):

    notice = Notice.objects.all().order_by('-Create_time')
    print(notice)

    context = { 'notifications': notice }

    return render(request, 'notifications.html', context)