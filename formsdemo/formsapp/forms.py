from django import forms
from django.core import validators

class UserRegistrationform(forms.Form):
    Gender =[('male','MALE'),('female','FEMALE')]
    fname = forms.CharField(max_length=35) # widget (it is used for difernt input type )
    lname = forms.CharField(max_length=25,validators=[validators.MinLengthValidator(6)])
    email = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=10,widget = forms.Select(choices =Gender))
    password = forms.CharField(widget=forms.PasswordInput)


'''
# single clean method 

    def clean(self):
        user_clean_data = super().clean()
        infname = user_clean_data['fname']
        inemail = user_clean_data['email']
        if len(infname)>20:
            raise forms.ValidationError("the max length is 20.")
        elif inemail.find('@') == -1:
            raise forms.ValidationError("the email should conntain @.")
        
'''

"""
# custom multi clean method

    def clean_fname(self):
        infnmae = self.cleaned_data['fname']
        if len(infnmae)>20:
            raise forms.ValidationError("the max length is 20.")
        return infnmae
    
    def clean_email(self):
        inemail = self.cleaned_data['email']
        if inemail.find('@') == -1:
            raise forms.ValidationError("the email should conntain @.")
        return inemail
    
    """

# from django import forms
# from django.core import validators

# class UserRegistrationForm(forms.Form):
#     Gender = [('male', 'MALE'), ('female', 'FEMALE')]
#     fname = forms.CharField(max_length=35)  # Widget can be used for different input types
#     lname = forms.CharField(max_length=25, validators=[validators.MinLengthValidator(6)])
#     email = forms.EmailField(max_length=254)  # Changed to EmailField for email validation
#     gender = forms.ChoiceField(choices=Gender, widget=forms.Select)
#     password = forms.CharField(widget=forms.PasswordInput)
