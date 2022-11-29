from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

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



def studentEditRequest(request,my_id):

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


def Editrecord(request,my_id):
    if("Edit" in request.POST):
        return update(request,my_id)
    elif("Delete" in request.POST):
        return delete(request, my_id)
    else:
        #change later
        return HttpResponseRedirect(reverse('adminHome'))


def update(request,my_id):
    member = database.objects.get(id=my_id)

    member.Teacher = request.POST['Teacher']
    member.Date = request.POST['Date']
    member.Time = request.POST['time']
    member.durations = request.POST['durations']
    member.lesson_type = request.POST['lesson_type']

    member.save()
    return HttpResponseRedirect(reverse('studentHome'))



def delete(request, my_id):
  member = database.objects.get(id=my_id)
  member.delete()
  return HttpResponseRedirect(reverse('studentHome'))



#function


#get requests for user

    

#get pending requests

# edit pending requests

# check if valid
#check terms in type
#

