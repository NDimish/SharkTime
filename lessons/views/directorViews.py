from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.utils.timezone import now

from ..forms import directorForms
from lessons.models import User as database
from lessons import models



def directorHomePage(request,Logged_ID):

   # obj =  database.objects.filter(Student = "testbob")
    
    data ={
        'name' : database.objects.get(id =Logged_ID).first_name,
        'Logged_ID' : Logged_ID
    }


    return render(request,'directorHome.html',data)



def FormRender( request,Logged_ID,my_id,inputform):

    if (my_id == -1):
        form = inputform(request.POST or None)
    else:
        form = inputform(request.POST or None, initial =inputform.objects.get(id=my_id))
    if form.is_valid():
        form.save(commit=True)

    data ={
        "form" : form,
        'Logged_ID' : Logged_ID
    }


    return render(request,'directorDataChange.html',data)






def UserFormPage(request,Logged_ID,my_id):


    return(FormRender( request,Logged_ID,my_id,models.User))


def StudentFormPage(request,Logged_ID,my_id):


    return(FormRender( request,Logged_ID,my_id,models.Student))

def DirectorFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Director))

def TeacherFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Teacher))

def PaymentFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Payment))

def Sys_userFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Sys_user))

def Sys_authorityFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Sys_authority))

def Sys_user_authorityFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Sys_user_authority))

def LessonFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Lesson))

def LessonRequestFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.LessonRequest))

def LessonBookingFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.LessonBooking))