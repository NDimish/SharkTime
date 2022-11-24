from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import User
from .requests import request
#helper file 
import helpers 
from django.utils.translation import gettext_lazy as _



#Booking model
class booking(models.Model):
    #unique booking_id 
    id = models.AutoField(primary_key=True)
    #request that the booking will fulfill
    request = models.ForeignKey(to=request , related_name = 'bookings', on_delete=models.Cascade )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    day_of_week = models.CharField(max_length=1,choices=helpers.DAY_OF_THE_WEEK)
    time_of_lesson = models.DecimalField(decimal_places = 2, max_digits= 4)
    teacher = models.CharField(max_length = 10)
    start_date = models.DateField(validators=[helpers.validateDate]) #front end use a Date Picker? 
    class LessonDuration(models.IntegerChoices):
        THIRTY_MINS = 30 , '30 minutes'
        FORTY_FIVE_MINS = 45 , '45 minutes'
        SIXTY_MINS = 60, '60 minutes'
    class LessonIntervals(models.IntegerChoices):
        ONCE_PER_WEEK = 1, '1 lesson every week'
        ONCE_PER_TWO_WEEKS  = 2, '1 lesson every 2 weeks'
    
    number_of_lessons = models.IntegerField(validators=[helpers.validateLessonNumber])
 


 # Note - To retrieve all bookings for a request, can use request.bookings 

   


 