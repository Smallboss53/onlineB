from dataclasses import fields
from tkinter import Y
from django.contrib.auth.models import User
from django_registration.forms import RegistrationForm
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm
#from . models import hotel_category

class signup_form(RegistrationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        for fieldname in ['username', 'password1','password2']:
            self.fields[fieldname].help_text = None
        self.helper.form_show_labels = True

class AvailabilityForm(forms.Form):
   
    check_in =forms.DateTimeField(required=True, input_formats=["%Y-%m-%dt%H:%M",])
    check_out =forms.DateTimeField(required=True, input_formats=["%Y-%m-%dt%H:%M",])

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class RegisterForm(RegistrationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.helper.form_show_labels = True 