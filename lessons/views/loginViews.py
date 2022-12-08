from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from ..forms.loginForms import signUp
from ..forms.loginForms import login
from django.urls import reverse
from django.utils.timezone import now
from lessons.models import User, Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as AuthLogin
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

def signUpPage(request):
    alert=""
    form = signUp(request.POST or None)
    #Creates a new user and redirects to home or shows an error if email used before
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
        userdata = get_user_model()
        formResult = form.save(commit=True)
        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                AuthLogin(request, user)
            else:
                alert = "user deactivated"    
            user1= userdata.objects.get(username = username)
            Logged_ID = user1.id
            #redirects the page based on the role
            if(formResult == 'S'):
                return HttpResponseRedirect(reverse('studentHome',args=(Logged_ID,)))
            elif(formResult == 'A'):
                return HttpResponseRedirect(reverse('adminHome'))
            elif(formResult == 'D'):
                return HttpResponseRedirect(reverse('directorHome',args=(Logged_ID,)))
            else:
                alert = "your not a decided user "
        else:
            alert = "Somthings wrong with your details"

    data ={
        'form':form,
        'alert':alert,}
    return render(request,'login.html',data)


def logoutPage(request):  
    logout(request)
    return HttpResponseRedirect(reverse('home' ))