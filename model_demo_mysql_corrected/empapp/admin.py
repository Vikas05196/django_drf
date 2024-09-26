from django.contrib import admin
from empapp.models import Empapp

# Register your models here.

class djangoadminpage(admin.ModelAdmin):
    list_display = ['fname','lname','salary','email'] # it will show all these column in django page.

admin.site.register(Empapp,djangoadminpage) # it will show the 
