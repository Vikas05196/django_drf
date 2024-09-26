from django.shortcuts import render

# Create your views here.

def rendertemplate(request):
    return render(request,'templates/firsttemplate.html')


def template_tags(request):
    mydict ={'name':'vikas'}
    return render(request,'templates/templatetags.html',context=mydict)

def electronics(request):
    mydict_2 ={
        'product1':'mac',
        'product2':'iphone',
        'product3':'samsung'
        }
    return render(request,'templates/product.html',context=mydict_2)

def toy(request):
    mydict_1 ={
        'product1':'toy car',
        'product2':'car',
        'product3':'toyota car'
        }
    return render(request,'templates/product.html',context=mydict_1)


def index(request):
    return render(request,'templates/index.html')




 
