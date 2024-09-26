# from django.shortcuts import render
# from modelforms import forms
# from modelforms.models import Project

from django.shortcuts import render
from .forms import ProjectForm
from .models import Project


# Create your views here.

def index(request):
    return render(request,'templates\index.html')

def listprojects(request):  # this view does 
    Project_list = Project.objects.all() ## the project_list give data in templates
    #listdict = {'Projectlist':Projectlist}
    return render(request,'listprojects.html',{'Project_list':Project_list})

# def addproject(request):
#     form = Project()
#     if request.method == 'POST':
#         form = Project(request.POST)
#         if forms.is_valid():
#             forms.save()
#         return index(request)
#     return render(request,'addproject.html',{'form':form})    


# from django.shortcuts import render
# from .forms import ProjectForm
# from .models import Project

def addproject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)  # Replace 'index' with your actual success URL or view name
    else:
        form = ProjectForm()
    
    projects = Project.objects.all()  # Fetch all projects to display in the table
    return render(request, 'addproject.html', {'form': form, 'projects': projects})



# from django.shortcuts import render, redirect
# from modelforms.forms import ProjectForm
# from modelforms.models import Project

# # Create your views here.

# def index(request):
#     return render(request, 'index.html')

# def listprojects(request):
#     project_list = Project.objects.all()
#     return render(request, 'listprojects.html', {'projects': project_list})

# def addproject(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')  # Redirect to the index view after saving
#     else:
#         form = ProjectForm()
#     return render(request, 'addproject.html', {'form': form})
