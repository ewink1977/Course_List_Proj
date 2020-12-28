from django.shortcuts import render, redirect, HttpResponse

def home(request):
    return render(request, 'html/home.html')

def add_course(request):
    pass
