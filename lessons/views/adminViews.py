#contains the views of the admin 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from lessons.forms import adminForms
from lessons.forms.adminForms import bookingForm as BookingForm , TermForm
from lessons.models import LessonBooking, LessonRequest, Student,Term
from django.http import Http404



"""
    Admin home view - This is the view displayed to the admin after logging in
    - Should display all student requests

"""
def admin_home(request):
    #Get all requests 
    requests = LessonRequest.objects.all()

    context = {'requests' : requests}
    #request_count = LessonRequest.objects.all().count()
    return render(request, 'adminHome.html', context)


#display all the term dates set
def view_term_dates(request):
    term_dates = Term.objects.all()
    context = {'terms' : term_dates}
    return render(request, 'adminViewTermDates.html', context)

#display all students in the school who have registered
def view_students(request):
    students = Student.objects.all()
    context = {'students' : students}
    return render(request, 'adminViewStudents.html', context)

#view an individual request
def view_request(request,id):
    #get the request from db with same pk as selected request
    a_request = LessonRequest.objects.get(pk=id)
    return HttpResponseRedirect(reverse ('adminHome.html')) 

#view request page 
def view_requests(request):
    #Get all requests 
    requests = LessonRequest.objects.all()

    context = {'requests' : requests}
    #request_count = LessonRequest.objects.all().count()
    return render(request, 'adminViewRequests.html', context)

#display all incoming transacions 
def view_transactions(request):
    students = Student.objects.all()
    context = {'students' : students}
    return render(request, 'adminViewTransactions.html',context)

#add a term
def add_term(request):
    form =TermForm(request.POST or None)
    if 'Submit' in request.POST:
       # booking = get_ob
        form = TermForm(request.POST)
        print (form.errors)
        if form.is_valid():
            form.save()
            #Redirect back to admin home page
            return redirect('/')
        print('invalid form')
    else :
        form = TermForm()
    
    context ={'form' : form }
    print("return render")
    return render(request, 'adminAddBooking.html', context)
#add a booking
def add_booking(request,id):
    corresponding_request = LessonRequest.objects.get(pk=id) 
    
    #Get the available days 
    form = BookingForm(request.POST or None)

    

    if 'Submit' in request.POST:
       # booking = get_ob
        form = BookingForm(request.POST)
        print (form.errors)
        if form.is_valid():
            corresponding_request.book_status = 'A'
            corresponding_request.save()
            form.save(commit=True)
            #Redirect back to admin home page
            return redirect('/')
        print('invalid form')
    elif 'Reject' in request.POST:
        form = BookingForm(request.POST)
        corresponding_request.book_status = 'R'
        corresponding_request.save()
        form.save(commit=True)
        #Redirect back to admin home page
        
        return redirect('/')

    else :
        form = adminForms.bookingForm( initial=get_init_booking_data(id))
    
    context ={'form' : form ,'request' : corresponding_request}
    print("return render")
    return render(request, 'adminAddBooking.html', context)

def edit_booking(request,id):
    try:
        obj = get_object_or_404(LessonBooking,request=id)
    except LessonBooking.DoesNotExist:
        raise Http404

    context ={
        'lesson_teacher': obj.lesson_teacher,
        'lesson_start_date': obj.lesson_start_date,
        'lesson_time': obj.lesson_time,
        'lesson_duration': obj.lesson_duration,
        'lesson_interval': obj.lesson_interval,
        'lesson_type':obj.lesson_type,
        'number_of_lessons':obj.number_of_lessons,
        
        }
    form  = BookingForm(request.POST or None , initial=context)
    data = {
        'data' : obj,
        'form' : form
    }
    return render(request, 'adminEditBooking.html', data)

def editBookingRecord(request,id):
    if('Update' in request.POST):
        return update(request,id)
    elif ('Delete in request.POST'):
        return delete(request,id)
    else:
        #change later
        return HttpResponseRedirect(reverse('studentHome'))

def update(request, id):
    member = LessonBooking.objects.get(pk=id)
    member.lesson_teacher = request.POST['lesson_teacher']
    member.lesson_start_date = request.POST['lesson_start_date_year'] + "-" + request.POST['lesson_start_date_month'] + "-" + request.POST['lesson_start_date_day']
    member.lesson_time = request.POST['lesson_time']
    member.lesson_duration = request.POST['lesson_duration']
    member.lesson_type = request.POST['lesson_type']
    member.number_of_lessons = request.POST['number_of_lessons']
    member.lesson_interval = request.POST['lesson_interval']
    member.save()
    return HttpResponseRedirect(reverse('adminHome'))

def delete(request, id):
  member = LessonBooking.objects.get(pk=id)
  
  request_id  = member.request.pk

  member.delete()
  corresponding_request = LessonRequest.objects.get(pk=request_id) 
  corresponding_request.book_status = 'P'
  corresponding_request.save()
  
  #Mark the corresponding request as unfulfilled 
  return HttpResponseRedirect(reverse('adminHome'))

"""
Create an initial booking object based on the request
"""
def get_init_booking_data(id):
    request = LessonRequest.objects.get(pk=id) 
    initial_data = {
        'request' : id,
        'lesson_teacher' : request.lesson_teacher ,
        'lesson_start_date' : request.lesson_start_date, 
        #add day_of_week
        'lesson_time' : request.lesson_time,
        'lesson_duration' : request.lesson_duration,
        'lesson_interval' : request.lesson_interval,
        'lesson_type' : request.lesson_type ,
        'number_of_lessons' : request.number_of_lessons

    }

    #print (request.availability)
    return initial_data




 