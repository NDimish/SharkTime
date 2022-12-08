from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.utils.timezone import now

from ..forms import directorForms
from lessons.models import User as database
from lessons import models
from lessons.forms import directorForms
from django.contrib.auth.decorators import login_required



def directorHomePage(request,Logged_ID):

   # obj =  database.objects.filter(Student = "testbob")
    
    data ={
        'name' : database.objects.get(id =Logged_ID).first_name,
        'Logged_ID' : Logged_ID,
        'value' : 0,
        'database':database.objects.filter()
    }


    return render(request,'directorHome.html',data)



def FormRender( request,Logged_ID,my_id,inputdatabase,formtype):
    alert = ""
    if (my_id == 0):
        form = formtype(request.POST or None)
    else:
        obj =  get_object_or_404(inputdatabase,id =my_id)
        form = formtype(request.POST or None, instance =obj)
    if form.is_valid():
        if("Edit" in request.POST):
            form.save()
            alert = "form saved"
        elif("Delete" in request.POST):
            instance = inputdatabase.objects.get(id=my_id)
            instance.delete()
            return HttpResponseRedirect(reverse('directorHome' , args =(Logged_ID,)) )
        elif("Create" in request.POST):
            form.save()
            return HttpResponseRedirect(reverse('directorHome' , args =(Logged_ID,)) )
    data ={
        "form" : form,
        'Logged_ID' : Logged_ID,
        'my_id' : my_id,
        "alert":alert
    }


    return render(request,'directorDataChange.html',data)






def UserFormPage(request,Logged_ID,my_id):


    return(FormRender( request,Logged_ID,my_id,models.User,directorForms.Userform))


def StudentFormPage(request,Logged_ID,my_id):


    return(FormRender( request,Logged_ID,my_id,models.Student,directorForms.Studentform))

def DirectorFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Director,directorForms.Directorform))

def TeacherFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Teacher,directorForms.Teacherform))

def PaymentFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Payment,directorForms.Paymentform))

def Sys_userFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Sys_user,directorForms.Sys_user_form))

def Sys_authorityFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Sys_authority,directorForms.Sys_authority_form))

def Sys_user_authorityFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Sys_user_authority,directorForms. Sys_user_authority_form))

def LessonFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Lesson,directorForms.Lessonsform))

def LessonRequestFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.LessonRequest,directorForms.LessonRequestform))

def LessonBookingFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.LessonBooking,directorForms.LessonBookingform))