from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from ..forms.studentforms import make_request
from ..models.requests import request as database

# Create your views here.
def studentHomePage(request):

    obj =  database.objects.filter(Student = "testbob")
    
    data ={
        'name' :'nathan',
        'booked_lessons' : obj
    
    }


    return render(request,'studentHome.html',data)



def studentMakeRequest(request):

    form = make_request(request.POST or None)
    if form.is_valid():
        form.save()
    data ={
        'form':form
    
    }


    return render(request,'request.html',data)



def studenEditRequest(request,my_id):

    try:
        obj = get_object_or_404(database,id=my_id)
    except database.DoesNotExist:
        raise Http404

    context ={
        'Teacher': obj.Teacher,
        'Date': obj.Date,
        'time': obj.time,
        'durations': obj.duration,
        'lesson_type':obj.lesson_type,
        }
    form = make_request(request.POST or None, initial = context)

   

    data ={
        'data':obj,
        'form':form

    }
    

    return render(request,'editrequest.html', data)






#function


#get requests for user
def get_requests():
    return 1
    

#get pending requests

# edit pending requests

# check if valid
#check terms in type
#

