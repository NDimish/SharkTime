from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.utils.timezone import now

from ..forms.studentforms import make_request
from ..models.models import LessonBook as database



def directorHomePage(request):

   # obj =  database.objects.filter(Student = "testbob")
    
    data ={
        'name' :'nathan',
        'Available_lessons' : [1,2,3,45,5,6,76,2,3,4,56,7,34,345,345,57,56634,54,5765,75,]
    
    }


    return render(request,'directorHome.html',data)