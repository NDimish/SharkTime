from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from ..forms.studentforms import make_request
from lessons.models import LessonRequest as database
from django.urls import reverse
from django.utils.timezone import now
from lessons.models import User, Student,Lesson
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def studentHomePage(request,Logged_ID):
    obj = User.objects.filter(id = Logged_ID).first()
    data = {
        'name' : obj.first_name , 
        'Available_lessons' : [23,3,4,4,2],
        'Logged_ID':Logged_ID
    }

    return render(request,'studentHome.html',data)

@login_required
def studentViewRequests(request,Logged_ID):
    obj = database.objects.all()
    #For now just get the first student in the database
    #student = User.objects.filter(role='S').first()
    student = Student.objects.first()
    print(student.pk, "says hello")
    s = student.pk
    print("student id is " , obj)
    Pending = database.objects.filter( book_status ="P")
    for book in Pending:
        if(now().date().today() > book.lesson_start_date):
            book.book_status = "R"
            #book.save()



    Pending = database.objects.filter(student_id= s, book_status ="P")

    Rejected = database.objects.filter(student_id= s, book_status ="R")
    Approved = database.objects.filter(student_id= s, book_status ="A")

    data ={
        'booked_lessons' : obj,
        'Pending_lessons':Pending,
        'Rejected_lessons':Rejected,
        'Accepted_lessons':Approved,
        'Logged_ID':Logged_ID,
    
    }
    return render(request,'studentViewRequests.html',data)    



#OTHER VERSION make_request
@login_required
def studentMakeRequest(request,Logged_ID):

    form = make_request(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse('studentViewRequests') ,Logged_ID = Logged_ID)
    data ={
        'form':form,
        'Logged_ID':Logged_ID

    }
    return render(request,'request.html',data)

    
@login_required
def studentEditRequest(request,Logged_ID,my_id):
    try:
        obj = get_object_or_404(database,id=my_id)
    except database.DoesNotExist:
        raise Http404
    if(obj.book_status != "P"):
        return HttpResponseRedirect(reverse('studentHome'), Logged_ID = Logged_ID)

    context ={
        'lesson_teacher': obj.lesson_teacher,
        'lesson_start_date': obj.lesson_start_date,
        'lesson_time': obj.lesson_time,
        'lesson_duration': obj.lesson_duration,
        'lesson_type':obj.lesson_type,
        'number_of_lessons':obj.number_of_lessons,
        'student_id':obj.student_id,
        'Logged_ID':Logged_ID
        }
    form = make_request(request.POST or None, initial = context)
   
    data ={
        'data':obj,
        'form':form,
        'Logged_ID':Logged_ID
    }
    
    return render(request,'editrequest.html', data)

@login_required
def Editrecord(request,Logged_ID,my_id):
    if("Edit" in request.POST):
        return update(request,my_id)
    elif("Delete" in request.POST):
        return delete(request, my_id)
    else:
        #change later
        return HttpResponseRedirect(reverse('studentHome'),Logged_ID = Logged_ID)




@login_required
def update(request,Logged_ID,my_id):
    member = database.objects.get(id=my_id)
    member.lesson_teacher = request.POST['lesson_teacher']
    member.lesson_start_date = request.POST['lesson_start_date']
    member.lesson_time = request.POST['lesson_time']
    member.lesson_duration = request.POST['lesson_duration']
    member.lesson_type = request.POST['lesson_type']
    member.number_of_lessons = request.POST['number_of_lessons']

    member.save()
    return HttpResponseRedirect(reverse('studentViewRequests'),Logged_ID = Logged_ID)


    
@login_required
def delete(request,Logged_ID, my_id):
  member = database.objects.get(id=my_id)
  member.delete()
  return HttpResponseRedirect(reverse('studentViewRequests'),Logged_ID = Logged_ID)



