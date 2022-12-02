from django import forms
from ..models import User
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


class SignUpForm(forms.ModelForm):
 class Meta:
  model = User
  fields = ['first_name', 'last_name', 'email', 'role']

 new_password = forms.CharField(
 label='Password',
 widget=forms.PasswordInput(),
 validators=[RegexValidator(
 regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
 message='Password must contain an uppercase character, a lowercase '
 'character and a number'
 )]
)
 password_confirmation = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())

 def clean(self):
  super().clean()
  new_password = self.cleaned_data.get('new_password')
  password_confirmation = self.cleaned_data.get('password_confirmation')
  if new_password != password_confirmation:
   self.add_error('password_confirmation', 'Confirmation does not match password.')

 def save(self):
     """Create a new user."""
     super().save(commit=False)
     user = User.objects.create_user(
         first_name=self.cleaned_data.get('first_name'),
         last_name=self.cleaned_data.get('last_name'),
         email=self.cleaned_data.get('email'),
         role=self.cleaned_data.get('role'),
     )
     return user


class LogInForm(forms.Form):
   email = forms.CharField(label="Email")
   password = forms.CharField(label="Password", widget=forms.PasswordInput())
   def save(self):
       """Create a new user."""
       super().save(commit=False)
       user = User.objects.create_user(
           first_name=self.cleaned_data.get('first_name'),
           last_name=self.cleaned_data.get('last_name'),
           email=self.cleaned_data.get('email'),
           role=self.cleaned_data.get('role'),
       )

       return user
