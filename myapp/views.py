from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("Hello Django")

# def homepage(request):
#     return HttpResponse("Homepage Content")

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def contactpage(request):
    return render(request, 'contact.html')