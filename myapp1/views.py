from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def signin(request):
    return render(request,'signin.html')

def courses(request):
    return render(request,'courses.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def callback(request):
    return render(request,'callback.html')

# Create your views here.
