from django.shortcuts import render,redirect
from ..forms.loginforms import LogInForm,SignUpForm
from django.contrib.auth import authenticate,login
from django.contrib import messages



def home(request):
 user=request.user
 return render(request, 'home.html',{'user:user'})

def sign_up(request):
 if request.method =='POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
        # form.save()
        return redirect('log_in')
 else:
     form=SignUpForm()
    # return render(request, 'home.html')
 return render(request, 'sign_up.html', {'form': form})

def log_in(request):
    if request.method =='POST':
       form = LogInForm(request.POST)
       if form.is_valid():
           #form.save()
           return redirect('student_home')
    else:
        form=LogInForm()
       # return render(request, 'home.html')
    return render(request, 'log_in.html', {'form': form})

def student_home(request):
    return render(request, 'student_home.html')
