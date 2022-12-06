from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from ..forms.loginForms import UserSignUpForm , UserLoginForm
from django.contrib.auth import login ,authenticate
from django.shortcuts import redirect
from lessons.models import User, Student,Client
from django.forms import forms, ValidationError

def register_user (request):
    form = UserSignUpForm()
    if request.method == "POST":
        form = UserSignUpForm(request.POST or None)
        if form.is_valid() :
            #get the role of the new user
            role = request.POST.get("is_client_or_student")
            #Make a student 
            if(role=="S"):
                user=form.save()
                s = Student()
                s.user = user
                s.save()
                redirect_url =  "/" 
                return redirect(redirect_url)
            
            #Make a client
            elif(role=="P"):
                user = form.save()
                p = Client()
                p.user = user
                p.save()
                redirect_url =  "/"
                return redirect(redirect_url) 


    context = {'form' : form}
    return render(request,'registerUser.html' ,context)

def login_user(request):
    
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get("email")
            user = authenticate(username=username,password=password)
            if user is not None:
                user = form.get_user()
                valid_user = User.objects.get(username=username)
                if valid_user.email == email:
                    login(request,user)
                    redirect_url = request.POST.get('next') or "/" 
                    return redirect(redirect_url)
                else :
                    print ("INCORRECT EMAIL ADDRESS")
    else:
        form = UserLoginForm(request)
    next = request.GET.get('next') or ''
    context = {'form' : form , 'next' : next}
    return render(request, "login.html",context )



def loginPage(request):
    alert=""
    form = login(request.POST or None)
    if form.is_valid():
        formResult = form.save(commit=True)
        if(formResult == "F"):
            alert = "Somthings wrong with your details"
        
        else:
            if(formResult == 'S'):
                return HttpResponseRedirect(reverse('studentHome'))
            elif(formResult == 'A'):
                return HttpResponseRedirect(reverse('adminHome'))
            elif(formResult == 'D'):
                return HttpResponseRedirect(reverse('directorHome'))        

    data ={
        'form':form,
        'alert':alert,

    }
    return render(request,'login.html',data)
