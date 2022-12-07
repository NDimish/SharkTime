from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.utils.timezone import now

from ..forms import directorForms
from lessons.models import User as database



def directorHomePage(request,Logged_ID):

   # obj =  database.objects.filter(Student = "testbob")
    
    data ={
        'name' : database.objects.get(id =Logged_ID).first_name,
        'Logged_ID' : Logged_ID
    }


    return render(request,'directorHome.html',data)


def UserFormPage(request,Logged_ID,my_id):


    form = directorForms.Userform(request.POST or None)
    if form.is_valid():
        form.save(commit=True)

    data ={
        "form" : form,
        'Logged_ID' : Logged_ID
    }


    return render(request,'directorDataChange.html',data)


def StudentFormPage(request,Logged_ID,my_id):


    form = directorForms.Studentform(request.POST or None)
    if form.is_valid():
        form.save(commit=True)

    data ={
        "form" : form,
        'Logged_ID' : Logged_ID
    }


    return render(request,'directorDataChange.html',data)

def DirectorFormPage(request,Logged_ID,my_id):


    form = directorForms.Directorform(request.POST or None, initial =Directormy_id)
    if form.is_valid():
        form.save(commit=True)

    data ={
        "form" : form,
        'Logged_ID' : Logged_ID
    }


    return render(request,'directorDataChange.html',data)