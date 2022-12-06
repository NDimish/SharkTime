from django import forms
from django.forms import ValidationError
from lessons.models import User
from lessons.models import Student as Student
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime


class UserSignUpForm(UserCreationForm):
   # email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
  
    
    class Meta():
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', "is_client_or_student" )
        #add labels here
        
        def clean_email(self):
            email = self.cleaned_data['email']
            obj = User.objects.get(email=email)
            if obj is not None:
                raise forms.ValidationError("This email is already associated with another account")

        
       

class UserLoginForm(AuthenticationForm):

    email = forms.EmailField(required=True, label="email")

