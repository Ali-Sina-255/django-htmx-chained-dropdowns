from django.shortcuts import render
from . models import Course, Module

def course(request):
    courses = Course.objects.all()
    context  = {
        "courses":courses
    }
    return render(request, 'university.html',context)


def modules_view(request):
    course = request.GET.get("course")
    print(course)
    modules = Module.objects.filter(course=course)
    print(modules)
    context = { "modules":modules}
    return render(request, 'partials/modules.html',context) 