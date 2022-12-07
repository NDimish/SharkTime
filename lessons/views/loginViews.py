from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from ..forms.loginForms import signUp
from ..forms.loginForms import login
from django.urls import reverse
from django.utils.timezone import now
from lessons.models import User, Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model

def signUpPage(request):
    alert=""
    form = signUp(request.POST or None)
    if form.is_valid():
        if(form.save(commit=True)):
            return HttpResponseRedirect(reverse('home'))
        else:
            alert = "Email already used"
    data ={
        'form':form,
        'alert':alert,

    }
    return render(request,'signUp.html',data)


def loginPage(request):
    alert=""
    form = login(request.POST or None)
    if form.is_valid():
        formResult = form.save(commit=True)
        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password = password)

        if(formResult == "F"):
            alert = "Somthings wrong with your details"
        else:
            user = get_user_model()
            user1= user.objects.get(username = username)
            Logged_ID = user1.id

            if(formResult == 'S'):
                return HttpResponseRedirect(reverse('studentHome',args=(Logged_ID,)))
            elif(formResult == 'A'):
                return HttpResponseRedirect(reverse('adminHome'))
            elif(formResult == 'D'):
                return HttpResponseRedirect(reverse('directorHome',args=(Logged_ID,)))        

    data ={
        'form':form,
        'alert':alert,}
    return render(request,'login.html',data)