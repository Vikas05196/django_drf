from django.shortcuts import render
from empapp.models import Empapp

# Create your views here.

def empdata(request):
    employee = Empapp.objects.all()
    empdict = {'employee':employee}
    return render(request,'templates/employees.html',context=empdict)


