from django.shortcuts import render

# Create your views here.
from .import forms

def uregview(request):
    form = forms.UserRegistrationform()
    if request.method == 'POST':
        form = forms.UserRegistrationform(request.POST)
        if form.is_valid():
            print("form is valid")
            print("fname",form.cleaned_data['fname'])
            print("lname",form.cleaned_data['lname'])
            print("email",form.cleaned_data['email'])
            print("gender",form.cleaned_data['gender'])
            print("password",form.cleaned_data['password'])



        return render(request,'templates/user_regs.html',{'form':form})

# from django.shortcuts import render
# from . import forms

# def uregview(request):
#     form = forms.UserRegistrationform()
#     if request.method == 'POST':
#         form = forms.UserRegistrationform(request.POST)
#         if form.is_valid():
#             print("form is valid")
#             print("fname:", form.cleaned_data['fname'])
#             print("lname:", form.cleaned_data['lname'])
#             print("email:", form.cleaned_data['email'])
    
#     return render(request, 'templates/user_regs.html', {'form': form})
