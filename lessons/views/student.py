from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from ..models.requests import Weekday
from ..forms.studentforms import make_request
from ..models.requests import request as database
from django.urls import reverse
from ..models import requests
from django.utils.timezone import now
from ..models.users import User, Student

# Create your views here.
def studentHomePage(request):
    obj = User.objects.get(role = 'S')
    data = {
        'name' : obj.first_name , 
        'Available_lessons' : [1,2,3,45,5,6,76,2,3,4,56,7,34,345,345,57,56634,54,5765,75,]
    }

    return render(request,'studentHome.html',data)

def studentViewRequests(request):
    obj = database.objects.filter(student_id =1)
    Pending = database.objects.filter(student_id = 1, status ="P")
    for book in Pending:
        if(now().date().today() > book.lesson_start_date):
            book.status = "R"
            #book.save()



    Pending = database.objects.filter(student_id = 1, status ="P")

    Rejected = database.objects.filter(student_id = 1, status ="R")
    Approved = database.objects.filter(student_id = 1, status ="A")

    data ={
        'booked_lessons' : obj,
        'Pending_lessons':Pending,
        'Rejected_lessons':Rejected,
        'Accepted_lessons':Approved,
    
    }
    return render(request,'studentViewRequests.html',data)    

def studentMakeRequest(request):

    form = make_request(request.POST or None)
    if request.method =="POST":
        form = make_request(request.POST)
        
        if form.is_valid():
        
            form.save(commit=True)
            return HttpResponseRedirect(reverse('studentViewRequests'))
            
    data ={
        'form':form,
    }


    return render(request,'request.html',data)


#OTHER VERSION make_request
# def studentMakeRequest(request):

#     form = make_request(request.POST or None)
#     if form.is_valid():
#         form.save(commit=True)
#         return HttpResponseRedirect(reverse('studentViewRequests'))
#     data ={
#         'form':form

#     }
#     return render(request,'request.html',data)

def studentEditRequest(request,my_id):
    try:
        obj = get_object_or_404(database,id=my_id)
    except database.DoesNotExist:
        raise Http404
    if(obj.status != "P"):
        return HttpResponseRedirect(reverse('studentHome'))

    context ={
        'lesson_teacher': obj.lesson_teacher,
        'lesson_start_date': obj.lesson_start_date,
        'lesson_time': obj.lesson_time,
        'lesson_duration': obj.lesson_duration,
        'lesson_type':obj.lesson_type,
        'number_of_lessons':obj.number_of_lessons,
        'student_id':obj.student_id
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
        return HttpResponseRedirect(reverse('studentHome'))





def update(request,my_id):
    member = database.objects.get(id=my_id)
    member.lesson_teacher = request.POST['lesson_teacher']
    member.lesson_start_date = request.POST['lesson_start_date']
    member.lesson_time = request.POST['lesson_time']
    member.lesson_duration = request.POST['lesson_duration']
    member.lesson_type = request.POST['lesson_type']
    member.number_of_lessons = request.POST['number_of_lessons']

    member.save()
    return HttpResponseRedirect(reverse('studentViewRequests'))


    

def delete(request, my_id):
  member = database.objects.get(id=my_id)
  member.delete()
  return HttpResponseRedirect(reverse('studentViewRequests'))



