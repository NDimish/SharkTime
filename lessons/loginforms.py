from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
 class Meta:
  model = User
  fields = ['first_name', 'last_name', 'email', 'role']

 new_password = forms.CharField(label='Password', widget=forms.PasswordInput())
 password_confirmation = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())

class LogInForm(forms.Form):
   email = forms.CharField(label="Email")
   password = forms.CharField(label="Password", widget=forms.PasswordInput())



