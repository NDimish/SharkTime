from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from .requests import request
#helper file 
from django.utils.translation import gettext_lazy as _
from lessons import helpers 
from ..models import requests
LESSON_DURATION_MAX_LENGTH=10
LESSON_INTERVAL_MAX_LENGTH=22

#Booking model
class booking(models.Model):
    #unique booking_id 
    id = models.AutoField(primary_key=True)
    #request that the booking will fulfill
    request = models.ForeignKey(to=request , related_name = 'bookings', on_delete=models.CASCADE )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    lesson_time = models.TimeField()
    lesson_type = models.CharField(max_length=1000, blank=False, default='instrument name here')
    lesson_teacher = models.CharField(max_length = 10)
    lesson_start_date = models.DateField(validators=[helpers.validateDate]) #front end use a Date Picker? 
 

    lesson_duration = models.IntegerField(choices=helpers.CHOICE_LESSON_DURATION,default=1,blank=False)
    lesson_interval = models.IntegerField(choices=helpers.CHOICE_LESSON_INTERVAL,default=1,blank=False)
    number_of_lessons = models.IntegerField(validators=[helpers.validateLessonNumber])
    objects = models.Manager() 

 # Note - To retrieve all bookings for a request, can use request.bookings 

   
