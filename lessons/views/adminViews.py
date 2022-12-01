#contains the views of the admin 
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from lessons.models.models import LessonBook as modelsrequests
from lessons.models.models import LessonConfirmed as modelsbooking
from lessons.forms import adminForms
from lessons.forms.adminForms import bookingForm as BookingForm


"""
    Admin home view - This is the view displayed to the admin after logging in
    - Should display all student requests

"""
def admin_home(request):
    #Get all requests 
    requests = modelsrequests.objects.all()
    context = {'requests' : requests}
    #request_count = models.request.objects.all().count()
    return render(request, 'adminHome.html', context)



    
def admin_view_students(request):
    return render(request, 'adminViewStudents.html')

def view_request(request,id):
    #get the request from db with same pk as selected request
    a_request = modelsrequests.objects.get(pk=id)
    return HttpResponseRedirect(reverse ('adminHome.html')) 

def make_booking(request, request_id):
    booking_request = modelsrequests.objects.get(pk=request_id)
    print("hello")
    print(booking_request.teacher)
    
    if request.method =='POST':
        
        form = adminForms.bookingForm(request.POST)
        
        print (form.errors)
        if form.is_valid():

          
            new_created_at = form.cleaned_data['created_at']
            new_updated_at = form.cleaned_data['updated_at']
            new_day_of_week = form.cleaned_data['day_of_week']
            new_time_of_lesson = form.cleaned_data['time_of_lesson']
            new_teacher = form.cleaned_data['teacher']
            new_start_date = form.cleaned_data['start_date']
            new_LessonDuration =  form.cleaned_data['LessonDuration']
            new_LessonIntervals = form.cleaned_data['LessonIntervals']
            new_number_of_lessons =  form.cleaned_data['number_of_lessons']
        new_booking = modelsbooking(
            new_created_at,
            new_updated_at,
            new_day_of_week,
            new_time_of_lesson ,
            new_teacher ,
            new_start_date,
            new_LessonDuration,
            new_LessonIntervals ,
            new_number_of_lessons 
        )
        #Create the new booking object
        new_booking.save()
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
    corresponding_request = modelsrequests.objects.get(pk=id) 
    form = BookingForm()
    print(" teacher is " , corresponding_request.lesson_type)
    if request.method == 'GET':
        form = adminForms.bookingForm(initial={'request' : id})
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print (form.errors)
        if form.is_valid():
            
            corresponding_request.status = 'A'
            corresponding_request.save()
            form.save()
            #Redirect back to admin home page
            print("hello")
            return redirect('/')
        #print('Printing post' , request.POST)
    context ={'form' : form ,'request' : corresponding_request}
    print("return render")
    return render(request, 'adminAddBooking.html', context)