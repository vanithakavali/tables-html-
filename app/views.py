from django.shortcuts import render
# Create your views here.
from app.models import *
def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)


def display_accessrecords(request):
    accessrecords=AccessRecords.objects.all()
    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecords.html',d)