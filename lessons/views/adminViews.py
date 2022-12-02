#contains the views of the admin 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
import lessons.models as models
from lessons.forms import adminForms
from lessons.forms.adminForms import bookingForm as BookingForm
from ..models import bookings
from ..models.bookings import booking
from django import forms
from django.http import Http404
from ..models import requests



"""
    Admin home view - This is the view displayed to the admin after logging in
    - Should display all student requests

"""
def admin_home(request):
    #Get all requests 
    requests = models.request.objects.all()

    context = {'requests' : requests}
    #request_count = models.request.objects.all().count()
    return render(request, 'adminHome.html', context)



    
def admin_view_students(request):
    return render(request, 'adminViewStudents.html')

def view_request(request,id):
    #get the request from db with same pk as selected request
    a_request = models.requests.objects.get(pk=id)
    return HttpResponseRedirect(reverse ('adminHome.html')) 




#add a booking
def add_booking(request,id):
    corresponding_request = models.requests.request.objects.get(pk=id) 
    #Get the available days 
    form = BookingForm(request.POST or None)
    #days=requests.request.objects.filter(pk = id).values_list('availability')
    #Filter the day_of_week field so that only days student marked as available can be booked
    #BookingForm.base_fields['day_of_week'] = forms.ModelMultipleChoiceField(queryset=requests.Weekday.objects.filter(pk__in=days), widget=forms.CheckboxSelectMultiple())   
    

    if 'Submit' in request.POST:
       # booking = get_ob
        form = BookingForm(request.POST)
        print (form.errors)
        if form.is_valid():
            corresponding_request.status = 'A'
            corresponding_request.save()
            form.save(commit=True)
            #Redirect back to admin home page
            return redirect('/')
        print('invalid form')
    elif 'Reject' in request.POST:
        form = BookingForm(request.POST)
        corresponding_request.status = 'R'
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
        obj = get_object_or_404(bookings.booking,request=id)
    except booking.DoesNotExist:
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
    member = booking.objects.get(pk=id)
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
  member = booking.objects.get(pk=id)
  
  request_id  = member.request.pk

  member.delete()
  corresponding_request = models.requests.request.objects.get(pk=request_id) 
  corresponding_request.status = 'P'
  corresponding_request.save()
  
  #Mark the corresponding request as unfulfilled 
  return HttpResponseRedirect(reverse('adminHome'))

"""
Create an initial booking object based on the request
"""
def get_init_booking_data(id):
    request = models.requests.request.objects.get(pk=id) 
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




 