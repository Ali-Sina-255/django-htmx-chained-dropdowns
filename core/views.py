from django.shortcuts import render
from . models import Course, Module
from .forms import UniversityForm

def course(request):
    form = UniversityForm()
    context  = {
        "form":form
    }
    return render(request, 'university.html',context)


def modules_view(request):
    course = request.GET.get("course")
    modules = Module.objects.filter(course=course)
    print(modules)
    context = {"modules":modules}
    return render(request, 'partials/modules.html',context) 