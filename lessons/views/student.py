from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.utils.timezone import now

from ..forms.studentforms import make_request
from ..models.models import LessonBook as database

# Create your views here.


# def login(view_function):
#    def mod_view(request):
#        if request.user.is_authenticated:
#            pass
#        else:
#            return view_function(request)




def studentHomePage(request):

   # obj =  database.objects.filter(Student = "testbob")
    
    data ={
        'name' :'nathan',
        'Available_lessons' : [1,2,3,45,5,6,76,2,3,4,56,7,34,345,345,57,56634,54,5765,75,]
    
    }


    return render(request,'studentHome.html',data)




def studentViewRequests(request):
    obj =  database.objects.filter(student_id = 1)
    Pending = database.objects.filter(student_id = 1, book_status ="P")
    for book in Pending:
        if(now().date().today() > book.book_date):
            book.book_status = "R"
            book.save()
       


    Pending = database.objects.filter(student_id = 1, book_status ="P")

    Rejected = database.objects.filter(student_id = 1, book_status ="R")
    Approved = database.objects.filter(student_id = 1, book_status ="A")
    
    data ={

        'booked_lessons' : obj,
        'Pending_lessons':Pending,
        'Rejected_lessons':Rejected,
        'Accepted_lessons':Approved,
    
    }


    return render(request,'studentViewRequests.html',data)    



    



def studentMakeRequest(request):

    form = make_request(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('studentVeiwRequests'))
    data ={
        'form':form
    
    }


    return render(request,'request.html',data)



def studentEditRequest(request,my_id):

    try:
        obj = get_object_or_404(database,id=my_id)
    except database.DoesNotExist:
        raise Http404
    if(obj.status != "P"):
        return HttpResponseRedirect(reverse('studentHome'))

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
        return HttpResponseRedirect(reverse('studentHome'))


def update(request,my_id):
    member = database.objects.get(id=my_id)

    member.Teacher = request.POST['Teacher']
    member.Date = request.POST['Date']
    member.Time = request.POST['time']
    member.durations = request.POST['durations']
    member.lesson_type = request.POST['lesson_type']

    member.save()
    return HttpResponseRedirect(reverse('studentVeiwRequests'))



def delete(request, my_id):
  member = database.objects.get(id=my_id)
  member.delete()
  return HttpResponseRedirect(reverse('studentVeiwRequests'))



#function


#get requests for user

    

#get pending requests

# edit pending requests

# check if valid
#check terms in type
#

