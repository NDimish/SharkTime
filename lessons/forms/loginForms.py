from django import forms
from lessons.models import User as sign
from lessons.models import Sys_user as User
from lessons.models import Student as Student
from django.utils.timezone import now
from django.db import models


class signUp(forms.Form):
  
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)
    nick_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
        
#labels = {'availability' : "Days You Are Available For Lessons"}  
#widgets = {'availability'  : forms.CheckboxSelectMultiple(attrs={'class' : 'form-control'}) }

    


    def save(self, commit=True):
        """Create a new user."""

        user1 = sign.objects.create(
        first_name = self.cleaned_data('first_name'),
        last_name = self.cleaned_data('last_name'),
        email = self.cleaned_data('email'),
        )

        sys_user1 = User.objects.create(
            user_name = (user1.first_name + user1.last_name+user1.id),
            password = self.cleaned_data('password'),
            salt = 123456,
            name = user1.first_name,
            create_time = now,
            update_time = now,
        )
        

        student1 = Student( user=user1)
        student1.created_at = now
        student1.updated_at = now
        student1.nick_name = self.cleaned_data('nick_name')
        student1.age = self.cleaned_data('age')
        student1.icon_url = "/user/a.jpg"
        student1.save()
        if commit:
            student1.save()
        return user1
        
