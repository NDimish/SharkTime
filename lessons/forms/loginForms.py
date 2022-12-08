from django import forms
from lessons.models import User as sign
from lessons.models import Sys_user as User
from lessons.models import Student as Student
from django.core.validators import RegexValidator
from django.utils.timezone import now
from django.db import models
import datetime


class signUp(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(label='Password',
    widget=forms.PasswordInput(),
    validators=[RegexValidator(
    regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
    message='Password must contain an uppercase character, a lowercase '
    'character and a number'
    )]
    )
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

    def save(self, commit=True):
        """Create a new user."""

        dataCheck = sign.objects.filter(email = self.cleaned_data.get('email'))
        if(dataCheck.count() >0):
            return False


        user1 = sign.objects.create_user(
        username = self.cleaned_data.get('email'),
        first_name = self.cleaned_data.get('first_name'),
        last_name = self.cleaned_data.get('last_name'),
        email = self.cleaned_data.get('email'),
        role = 'S',
        password=self.cleaned_data.get('password'),
        is_active = True,
        )
        #user1.set_password(self.cleaned_data.get('password'))
        user1.save()

        student1 = Student.objects.create(
            user=user1,
            created_at = now,
            nick_name = self.cleaned_data.get('nick_name'),
            age = self.cleaned_data.get('age'),
        )
        return True

class login(forms.Form):

    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())

    class Meta:
        fields=(
            "email",
            "password",
        )

    def save(self, commit=True):
        userCheck = sign.objects.filter(email = self.cleaned_data.get('email'))
        return userCheck[0].role



