from django.shortcuts import render
from django.http import HttpResponse
from .models import Images
# Create your views here.

def home(request):
    return render(request,'homey.html')

def about(request):
    return render(request,'about.html')


def gallery(request):
    video=Images.objects.all()
    return render(request,"gallery.html",{"video":video})

def contact(request):
    return render(request,'contact.html')

def clips(request):
    return render(request,'clips.html')


def services(request):
    return render(request,'services.html')