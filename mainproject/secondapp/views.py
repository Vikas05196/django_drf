from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def display_second(request):
     return HttpResponse("this is my second  program in django....")

