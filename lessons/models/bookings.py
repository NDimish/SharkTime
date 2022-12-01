# from django.db import models
# from django.utils.timezone import now
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .users import User
# from .requests import request
# #helper file 
# from lessons import helpers 
# from django.utils.translation import gettext_lazy as _

# LESSON_DURATION_MAX_LENGTH=10
# LESSON_INTERVAL_MAX_LENGTH=22

# #Booking model
# class booking(models.Model):
#     #unique booking_id 
#     id = models.AutoField(primary_key=True)
#     #request that the booking will fulfill
#     request = models.ForeignKey(to=request , related_name = 'bookings', on_delete=models.CASCADE )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now = True)

#     day_of_week = models.IntegerField(choices=helpers.DAY_OF_THE_WEEK)
#     time_of_lesson = models.DecimalField(decimal_places = 2, max_digits= 4)
#     teacher = models.CharField(max_length = 10)
#     start_date = models.DateField(validators=[helpers.validateDate]) #front end use a Date Picker? 
#     # class LessonDuration(models.IntegerChoices):
#     #     THIRTY_MINS = 30 , '30 minutes'
#     #     FORTY_FIVE_MINS = 45 , '45 minutes'
#     #     SIXTY_MINS = 60, '60 minutes'
#     # class LessonIntervals(models.IntegerChoices):
#     #     ONCE_PER_WEEK = 1, '1 lesson every week'
#     #     ONCE_PER_TWO_WEEKS  = 2, '1 lesson every 2 weeks'
#     CHOICE_LESSON_DURATION = ((1 , '30 minutes'),(2 , '45 minutes'), (3, '60 minutes'))
#     CHOICE_LESSON_INTERVAL = ((1, '1 lesson every week'), (2, '1 lesson every 2 weeks'))

#     lesson_duration = models.IntegerField(choices=CHOICE_LESSON_DURATION,default=1,blank=False)
#     lesson_interval = models.IntegerField(choices=CHOICE_LESSON_INTERVAL,default=1,blank=False)
#    # lesson_duration = models.CharField(max_length=LESSON_DURATION_MAX_LENGTH, choices=LessonDuration.choices, default=LessonDuration.THIRTY_MINS)
#     #lesson_interval = models.CharField(max_length=LESSON_INTERVAL_MAX_LENGTH,choices=LessonIntervals.choices,default=LessonIntervals.ONCE_PER_WEEK)
#     number_of_lessons = models.IntegerField(validators=[helpers.validateLessonNumber])
#     objects = models.Manager() 

 # Note - To retrieve all bookings for a request, can use request.bookings 

   


 