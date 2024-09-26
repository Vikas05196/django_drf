from django.shortcuts import render
#from .models import students
#from .forms import Student_form
# Create your views here.

from .forms import Student_form
from .models import students


def getstudent(request):
    student = students.objects.all()
    return render(request,'index.html',{'students':student})


def create_student(request):
    form = Student_form()
    if request.method =="POST":
        form = Student_form(request.POST)
        if form.is_valid():
            form.save()
        return('/')
    return render (request,'create.html',{'form':form})    