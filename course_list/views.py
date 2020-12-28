from course_list.models import Courses, Descriptions
from django.shortcuts import render, redirect, HttpResponse

def home(request):
    context = {
        "courses" : Courses.objects.all(),
        "descriptions" : Descriptions.objects.all(),
    }
    return render(request, 'html/home.html', context)

def add_course(request):
    if request.method == 'POST':
        newcourse = Courses.objects.create(name=request.POST['coursename'])
        Descriptions.objects.create(desc=request.POST['coursedesc'], course=newcourse)
        return redirect('home')

def destroy_course(request, killid):
    if request.method == 'GET':
        context = {
            'killinfo' : Courses.objects.get(id=killid)
        }
        return render(request, 'html/destroy.html', context)
    if request.method == 'POST':
        byebye = Courses.objects.get(id=killid)
        byebye.delete()
        return redirect('home')
