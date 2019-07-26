from django.shortcuts import render,get_list_or_404
import markdown
from .models import Notice
# Create your views here.
def index(request):
    notifications=get_list_or_404(Notice)
    for notification in notifications:
        print(notification)
        notification.content=markdown.markdown(notification.content,extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',])

    return render(request,"notification.html",context={"notifications":notifications})