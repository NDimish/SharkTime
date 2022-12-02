#contains the views of the admin 
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
import lessons.models as models
from lessons.forms import adminForms
from lessons.forms.adminForms import bookingForm as BookingForm
from ..models import bookings
from django import forms
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

def make_booking(request, request_id):
    booking_request = models.requests.objects.get(pk=request_id)
    print("hello")
    print(booking_request.teacher)
    form = adminForms.bookingForm(request.POST or None )
    if request.method =='POST':
        
        form = adminForms.bookingForm(request.POST)
        
        print (form.errors)
        if form.is_valid():
            form.save(commit=True)
        
        #mark request as fulfilled  if not already 

        
        if( not booking_request.isFulfilled):
           booking_request.markAsFulfilled  
        
        return render(request,'adminAddBooking.html', {
            #'id' : id,
            'form' : adminForms.bookingForm(request_id),
            'success' : True
        })

    else:
        form = adminForms.bookingForm(request_id)
        print("hello there")
    return render(request, 'adminAddBooking.html',{
       # 'id' : id,
        'form' : adminForms.bookingForm(request_id)
    })




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

"""
Create an initial booking object based on the request
"""
def get_init_booking_data(id):
    request = models.requests.request.objects.get(pk=id) 
    initial_data = {
        'request' : id,
        'teacher' : request.lesson_teacher ,
        #'time_of_lesson' : request. ,
        'start_date' : request.lesson_start_date, 
        #add day_of_week
        'lesson_time' : request.lesson_time,
        'lesson_duration' : request.lesson_duration,
        'lesson_interval' : request.lesson_interval,
        'lesson_type' : request.lesson_type ,
        'number_of_lessons' : request.number_of_lessons

    }

    #print (request.availability)
    return initial_data




 