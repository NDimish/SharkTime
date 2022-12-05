from django import forms
from lessons.models import User as sign
from lessons.models import Sys_user as User
from lessons.models import Student as Student
from django.utils.timezone import now
from django.db import models
import datetime


class signUp(forms.Form):
  
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)
    nick_name = forms.CharField(max_length=50)
    age = forms.IntegerField()

    class Meta:
        fields=(

            "first_name",
            "last_name", 
            "email ",
            "password ",
            "nick_name", 
            "age", 

        )
        
#labels = {'availability' : "Days You Are Available For Lessons"}  
#widgets = {'availability'  : forms.CheckboxSelectMultiple(attrs={'class' : 'form-control'}) }

    


    def save(self, commit=True):
        """Create a new user."""

        dataCheck = sign.objects.filter(email = self.cleaned_data.get('email'))
        if(dataCheck.count() >0):
            return False

        user1 = sign.objects.create(
        first_name = self.cleaned_data.get('first_name'),
        last_name = self.cleaned_data.get('last_name'),
        email = self.cleaned_data.get('email'),
        role = 'S',
        )


        sys_user1 = User.objects.create(
            user_name = (user1.first_name + user1.last_name + str(user1.id)),
            user = user1,
            password = self.cleaned_data.get('password'),
            salt = 123456,
            name = self.cleaned_data.get('first_name'),
            create_time = now(),
            update_time = now(),
        )
        

        student1 = Student.objects.create( 
            user=user1,
            created_at = now,
            updated_at = now,
            nick_name = self.cleaned_data.get('nick_name'),
            age = self.cleaned_data.get('age'),
            icon_url = "/user/a.jpg",
        )

        return True
        


class login(forms.Form):
  

    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)


    class Meta:
        fields=(


            "email ",
            "password ",


        )
        
#labels = {'availability' : "Days You Are Available For Lessons"}  
#widgets = {'availability'  : forms.CheckboxSelectMultiple(attrs={'class' : 'form-control'}) }

    


    def save(self, commit=True):
        userCheck = sign.objects.filter(email = self.cleaned_data.get('email'))
        if(userCheck.count() <1):
            return "F"
        
        passwordCheck = User.objects.filter(user = userCheck[0])
        if(passwordCheck[0].password == self.cleaned_data.get('password')):
             return userCheck[0].role
        return "F" 