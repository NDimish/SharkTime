#contains the views of the admin 
from django import urls
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from lessons.forms import adminForms
from lessons.forms.adminForms import bookingForm as BookingForm , TermForm
from lessons.models import LessonBooking, LessonRequest, Student,Term
from django.contrib.auth.decorators import login_required 
from django.http import Http404
from lessons import schedule
from lessons.views.student import viewInvoice

from django.contrib import messages
from django.utils.timezone import now
"""
    Admin home view - This is the view displayed to the admin after logging in
    - Should display all student requests

"""
#@login_required
def admin_home(request):
    current_user = request.user
    #Get all requests 
    requests = LessonRequest.objects.all()

    context = {'requests' : requests}
    #request_count = LessonRequest.objects.all().count()
    return render(request, 'adminHome.html', context)

#display all students in the school who have registered
#@login_required
def view_students(request):
    current_user = request.user
    students = Student.objects.all()
    context = {'students' : students}
    return render(request, 'adminViewStudents.html', context)

#@login_required
#view an individual request
def view_request(request,id):
    #get the request from db with same pk as selected request
    a_request = LessonRequest.objects.get(pk=id)
    return HttpResponseRedirect(reverse ('adminHome.html'))

#@login_required
#view request page 
def view_requests(request):
    #Get all requests
    requests = LessonRequest.objects.all()
    context = {'requests' : requests}
    #request_count = LessonRequest.objects.all().count()
    return render(request, 'adminViewRequests.html', context)
#@login_required
#display all incoming transacions 
def view_transactions(request):
    students = Student.objects.all()
    context = {'students' : students}
    return render(request, 'adminViewTransactions.html',context)

#@login_required
#add a booking
def add_booking(request,id):
    corresponding_request = LessonRequest.objects.get(pk=id)

    #Get the available days
    form = BookingForm(request.POST or None)

    if 'CustomBook' in request.POST:
       # booking = get_ob
        form = BookingForm(request.POST)
        print (form.errors)
        if form.is_valid():
            corresponding_request.book_status = 'A'
            corresponding_request.save()
            lesson_start_date = request.POST['lesson_start_date_year'] + "-" + request.POST['lesson_start_date_month'] + "-" + request.POST['lesson_start_date_day']
            lesson_end_date = request.POST['lesson_end_date_year'] + "-" + request.POST['lesson_end_date_month'] + "-" + request.POST['lesson_end_date_day']
            num_of_lessons = request.POST['number_of_lessons']
            day_of_week = request.POST["lesson_day_of_week"]
            lesson_interval = request.POST['lesson_interval']
            date_list = schedule.getDateListOfScheduleForNewTerm(None, num_of_lessons,lesson_start_date,lesson_end_date,day_of_week,lesson_interval)
            # for i in date_list:
            #     print ( i  ,day_of_week )
            booking = form.save(commit=False)
            #Update the number of lessons booked 
            booking.number_of_lessons = len(date_list)
 
            form.save(commit=True)
            #Redirect back to admin home page
            return redirect('/')
        print('invalid form')
    elif 'DefaultBook' in request.POST :
        #for default booking, need to get the current term 
        form = BookingForm(request.POST)
        print (form.errors)
        if form.is_valid():
            
            num_of_lessons = request.POST['number_of_lessons']
            day_of_week = request.POST["lesson_day_of_week"]
            lesson_interval = request.POST['lesson_interval']
            lesson_start_date = request.POST['lesson_start_date_year'] + "-" + request.POST['lesson_start_date_month'] + "-" + request.POST['lesson_start_date_day']
            #if the given start date is during a term, then book for the remaining term 
            if(schedule.checkIfDateDuringTerm(lesson_start_date)):
                term = schedule.getCurrentTermFromDate(lesson_start_date)
                if term is not None:
                    date_list = schedule.getDateListOfScheduleForNewTerm(term, num_of_lessons, lesson_start_date, None , day_of_week, lesson_interval ) 
                    # for i in date_list:
                    #     print ( i  ,day_of_week )
                    booking = form.save(commit=False)
                    #Update the number of lessons booked 
                    booking.number_of_lessons = len(date_list)
                    if lesson_start_date==None:
                        booking.lesson_start_date = term.start_of_term_date 
                    #Because default booking method was selected, the lesson end date will be the end of term
                    booking.lesson_end_date = term.end_of_term_date 
        
                    corresponding_request.book_status = 'A'
                    corresponding_request.save()

                    form.save(commit=True)
                    #Redirect back to admin home page
                    return redirect('/')
                else:
                    pass
                    #display a msg saying the booking was not possible ,retunr 
            #if the lesson is not during term 
                #need admin to specify a start date and then we will book for remaining term 
                    
            else :
               #otherwise just get the next upcoming term and book lessons in that term 
               term = schedule.getNearestTerm(lesson_start_date)
               if term is not None :
                    date_list = schedule.getDateListOfScheduleForNewTerm(term, num_of_lessons , None, None, day_of_week, lesson_interval)
                    # for i in date_list:
                    #     print ( i  ,day_of_week )
                    booking = form.save(commit=False)
                    #Update the number of lessons booked 
                    booking.number_of_lessons = len(date_list)
                    booking.lesson_start_date = term.start_of_term_date
                    booking.lesson_end_date = term.end_of_term_date
                    form.save(commit=True)
                    corresponding_request.book_status = 'A'
                    corresponding_request.save()
      
                    form.save(commit=True)
                    #Redirect back to admin home page
                    return redirect('/')
                    
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

def view_schedule(request,id) : 
    try:
        booking = LessonBooking.objects.filter(request=id).order_by('-id').first()
        req = LessonRequest.objects.get(pk=id)
       # booking = get_object_or_404(LessonBooking,request=id)
    except LessonBooking.DoesNotExist:
        raise Http404
    #Get the booking for which you want to see the schedule  
    #booking = LessonBooking.objects.get(pk=id)
    #get the date list which will be passed to the template
    date_list = schedule.getDateListGivenASchedule(booking.number_of_lessons, booking.lesson_start_date,booking.lesson_end_date, booking.lesson_day_of_week, booking.lesson_interval)
    #term = schedule.getCurrentTermFromDate(booking.lesson_start_date)
    
    context = {'booking' : booking , 'date_list' : date_list, 'request' : req} #'term' : term}
    return render(request, "viewLessonSchedule.html", context)

#@login_required
def edit_booking(request,id):
    try:
        obj = LessonBooking.objects.filter(request=id).order_by('-id').first()
    except LessonBooking.DoesNotExist:
        raise Http404

    context ={
        'lesson_teacher': obj.lesson_teacher,
        'lesson_start_date': obj.lesson_start_date,
        'lesson_time': obj.lesson_time,
        'lesson_duration': obj.lesson_duration,
        'lesson_interval': obj.lesson_interval,
        'lesson_day_of_week': obj.lesson_day_of_week,
        'lesson_type':obj.lesson_type,
        'number_of_lessons':obj.number_of_lessons,

        }
    form  = BookingForm(request.POST or None , initial=context)
    if form.is_valid():
        if('Update' in request.POST):
            return update(request,id)
        elif ('Delete in request.POST'):
            return delete(request,id)
    # else:
    #     #change later
    #     return HttpResponseRedirect(reverse('adminHome'))
    data = {
        'data' : obj,
        'form' : form
    }
    return render(request, 'adminEditBooking.html', data)
#@login_required
def editBookingRecord(request,id):
    if('Update' in request.POST):
        return update(request,id)
    elif ('Delete in request.POST'):
        return delete(request,id)
    else:
        #change later
        return HttpResponseRedirect(reverse('adminHome'))

#@login_required
def update(request, id):
    member = LessonBooking.objects.get(pk=id)
    member.lesson_teacher = request.POST['lesson_teacher']
    member.lesson_start_date = request.POST['lesson_start_date_year'] + "-" + request.POST['lesson_start_date_month'] + "-" + request.POST['lesson_start_date_day']
    member.lesson_time = request.POST['lesson_time']
    member.lesson_duration = request.POST['lesson_duration']
    member.lesson_type = request.POST['lesson_type']
    member.number_of_lessons = request.POST['number_of_lessons']
    member.lesson_interval = request.POST['lesson_interval']
    member.lesson_day_of_week = request.POST['lesson_day_of_week']
    member.save()
    return HttpResponseRedirect(reverse('adminHome'))
#@login_required
def delete(request, id):
  member = LessonBooking.objects.get(pk=id)
  #corresponding_request = LessonRequest.objects.get(pk=id) 
    
  request_obj = member.request
  corresponding_request = request_obj

  corresponding_request.book_status = 'P'
  corresponding_request.save()
  member.delete()

  
  #Mark the corresponding request as unfulfilled 
  return HttpResponseRedirect(reverse('adminHome'))


"""
Create an initial booking object based on the request
"""
#@login_required
def get_init_booking_data(id):
    request = LessonRequest.objects.get(pk=id)
    initial_data = {
        'request' : id,
        'lesson_teacher' : request.lesson_teacher ,
        'lesson_start_date' : request.lesson_start_date, 
         'lesson_day_of_week' : request.lesson_day_of_week , 
        'lesson_time' : request.lesson_time,
        'lesson_duration' : request.lesson_duration,
        'lesson_interval' : request.lesson_interval,
        'lesson_type' : request.lesson_type ,
        'number_of_lessons' : request.number_of_lessons

    }

    #print (request.availability)
    return initial_data

#display all the term dates set
def view_term_dates(request):
    term_dates = Term.objects.all()
    context = {'terms' : term_dates}
    return render(request, 'adminViewTermDates.html', context)

#add a term
def add_term(request):
    form =TermForm(request.POST or None)
    if 'Submit' in request.POST:
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
    return render(request, 'adminAddTermDates.html', context)

def edit_term(request,id):
    try:
        obj = get_object_or_404(Term,pk=id)
    except Term.DoesNotExist:
        raise Http404

    context ={
        'name': obj.name,
        'start_of_term_date': obj.start_of_term_date,
        'end_of_term_date': obj.end_of_term_date,
        
        }
    form  = TermForm(request.POST or None , initial=context)
    data = {
        'data' : obj,
        'form' : form
    }
    return render(request, 'adminEditTermDates.html', data) 

#edit the selected term where id is the id of the selected term
def edit_a_term(request, id):
    if('Update' in request.POST):
        return update_term(request,id)
    elif ('Delete' in request.POST):
        return delete_term(request,id)
    else:
        #change later
        return HttpResponseRedirect(reverse('adminViewTermDates'))

def update_term(request,id):

    term = Term.objects.get(pk=id)
    if request.method == 'POST':
        if "Update" in request.POST:
            form = TermForm(request.POST, instance=term)
            if form.is_valid():
                # if term.created_at:
                count_names = Term.objects.filter(name=term.name).exclude(pk=id).count()
                if count_names==0:
                    #now check if the there are any date overlaps excluding the current term instance
                    overlap_start_count = Term.objects.filter(start_of_term_date__gte = term.start_of_term_date , start_of_term_date__lte=term.end_of_term_date).exclude(pk=id).count()
                    overlap_end_count =  Term.objects.filter(end_of_term_date__gte = term.start_of_term_date, end_of_term_date__lte=term.end_of_term_date).exclude(pk=id).count()
                    overlap_count = overlap_start_count > 0 or overlap_end_count> 0
                    if overlap_count == 0 : 
                        if term.start_of_term_date<term.end_of_term_date:
                            form.save()
                            return redirect('adminViewTermDates')
        elif "Delete" in request.POST:
            term.delete()
            return redirect('adminViewTermDates')
    else:
        form = TermForm(instance=term)
    return render (request, 'adminEditTermDates.html', {'form' : form , 'id' : id  })

def delete_term(id): 
    term = Term.objects.get(pk=id)
    
    term.delete()
    return HttpResponseRedirect(reverse('adminHome'))

