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


@login_required
def directorHomePage(request,Logged_ID):

   # obj =  database.objects.filter(Student = "testbob")
    
    data ={
        'name' : database.objects.get(id =Logged_ID).first_name,
        'Logged_ID' : Logged_ID,
        'value' : 0,
        'database':database.objects.filter()
    }


    return render(request,'directorHome.html',data)


@login_required
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


@login_required
def ShowRender( request,Logged_ID,inputdatabase,pagetype,url):

    data ={
        "URL" :url,
        "text" : pagetype,
        'Logged_ID' : Logged_ID,
        "database":inputdatabase.objects.filter(),
        "value":0
    }
    return render(request,'directorSeeData.html',data)



@login_required
def UserFormPage(request,Logged_ID,my_id):


    return(FormRender( request,Logged_ID,my_id,models.User,directorForms.Userform))

@login_required
def StudentFormPage(request,Logged_ID,my_id):


    return(FormRender( request,Logged_ID,my_id,models.Student,directorForms.Studentform))


@login_required
def DirectorFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Director,directorForms.Directorform))


@login_required
def TeacherFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Teacher,directorForms.Teacherform))


@login_required
def PaymentFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Payment,directorForms.Paymentform))


@login_required
def Sys_userFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Sys_user,directorForms.Sys_user_form))


@login_required
def Sys_authorityFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Sys_authority,directorForms.Sys_authority_form))


@login_required
def Sys_user_authorityFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Sys_user_authority,directorForms. Sys_user_authority_form))


@login_required
def LessonFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.Lesson,directorForms.Lessonsform))


@login_required
def LessonRequestFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.LessonRequest,directorForms.LessonRequestform))


@login_required
def LessonBookingFormPage(request,Logged_ID,my_id):

    return(FormRender( request,Logged_ID,my_id,models.LessonBooking,directorForms.LessonBookingform))








@login_required
def UserShowPage(request,Logged_ID,):


    return(ShowRender( request,Logged_ID,models.User,"user",'UserFormPage'))



@login_required
def StudentShowPage(request,Logged_ID,):


    return(ShowRender( request,Logged_ID,models.Student,"student",'StudentFormPage'))


@login_required
def DirectorShowPage(request,Logged_ID,):

    return(ShowRender( request,Logged_ID,models.Director,"Director",'DirectorFormPage'))


@login_required
def TeacherShowPage(request,Logged_ID,):

    return(ShowRender( request,Logged_ID,models.Teacher,"Teacher",'TeacherFormPage'))


@login_required
def PaymentShowPage(request,Logged_ID,):

    return(ShowRender( request,Logged_ID,models.Payment,"Payment",'PaymentFormPage'))


@login_required
def Sys_userShowPage(request,Logged_ID,):

    return(ShowRender( request,Logged_ID,models.Sys_user,"Sys_user",'Sys_userFormPage'))


@login_required
def Sys_authorityShowPage(request,Logged_ID,):

    return(ShowRender( request,Logged_ID,models.Sys_authority,"Authorities",'Sys_authorityFormPage'))


@login_required
def Sys_user_authorityShowPage(request,Logged_ID,):

    return(ShowRender( request,Logged_ID,models.Sys_user_authority,"UserAuthorities",'Sys_user_authorityFormPage'))


@login_required
def LessonShowPage(request,Logged_ID,):

    return(ShowRender( request,Logged_ID,models.Lesson,"lessons",'LessonFormPage'))


@login_required
def LessonRequestShowPage(request,Logged_ID,):

    return(ShowRender( request,Logged_ID,models.LessonRequest,"lesson Requests",'LessonRequestFormPage'))


@login_required
def LessonBookingShowPage(request,Logged_ID,):

    return(ShowRender( request,Logged_ID,models.LessonBooking,"lesson booked",'LessonBookingFormPage'))