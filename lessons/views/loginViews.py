from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from ..forms.loginForms import signUp
from django.urls import reverse
from django.utils.timezone import now
from lessons.models import User, Student

def signUpPage(request):
    form = signUp(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse('home'))
    data ={
        'form':form

    }
    return render(request,'signUp.html',data)
