from course_list.models import Courses, Descriptions
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    context = {
        "courses" : Courses.objects.all(),
        "descriptions" : Descriptions.objects.all(),
    }
    return render(request, 'html/home.html', context)

def add_course(request):
    if request.method == 'POST':
        errors = Courses.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='danger')
            return redirect('home')
        else:
            newcourse = Courses.objects.create(name=request.POST['coursename'])
            Descriptions.objects.create(desc=request.POST['coursedesc'], course=newcourse)
            messages.success(request, f"{ request.POST['coursename'] } has been created successfully!")
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