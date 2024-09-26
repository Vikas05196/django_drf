from django import forms 
from fbvapp import students

class Student_form(forms.ModelForm):
    class Meta:
        model = 'students'
        fields = '__all__'