from django.db import models
from django.utils.timezone import now
from lessons import helpers
from .users import Student 
from .users import User

from django.utils.translation import gettext as _
from django.contrib import admin
from django import forms

DAY_OF_WEEK_CHOICES = (('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),)
class Weekday(models.Model):
    MONDAY = 1
    TUESDAY= 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5

    WEEKDAY_CHOICES = (
        (MONDAY, _('Monday')),
        (TUESDAY, _('Tuesday')),
        (WEDNESDAY, _('Wednesday')),
        (THURSDAY, _('Thursday') ),
        (FRIDAY, _('Friday')),
    )

    
    weekday = models.IntegerField(choices=WEEKDAY_CHOICES, default=1) 


    day = models.IntegerField(_('Days'),
                        choices=WEEKDAY_CHOICES, blank=True , unique=True)
    def __str__(self):
        return self.get_day_display()



class requestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }




class request(models.Model):
    """
    FROM EPIC 1 :  A REQUEST SHOULD HAVE 
    student's availability - days of the week  ? 
    number of lessons
    interval between lessons
    duation of each lesson
    Name of the teacher
    Lesson type
    Student id - display the students' name 
    """
    REQUEST_STATUS_CHOICES = (
        ('P', 'Pending'),
        ('R', 'Rejected'),
        ('A', 'Accepted'),
        ('O', 'Old'),
    )

    date_sent = models.DateField(default = now)

    student_id = models.ForeignKey(to=Student, related_name = 'request', on_delete=models.CASCADE )
    status = models.CharField(max_length=1, blank=False, choices = REQUEST_STATUS_CHOICES, default='P')
    lesson_time = models.TimeField(default=now)
    lesson_interval = models.IntegerField(blank=False,choices=helpers.CHOICE_LESSON_INTERVAL, default=1 )
    lesson_duration = models.IntegerField(blank=False, choices=helpers.CHOICE_LESSON_DURATION, default=1)
    number_of_lessons = models.IntegerField(validators=[helpers.validateLessonNumber])
    lesson_teacher = models.CharField(max_length = 20, default='')
    lesson_type = models.CharField(max_length=1000, blank=False, default='instrument name here')
    lesson_start_date = models.DateField(default = now)

    #availability = models.ManyToManyField(Weekday)

    def isFulfilled(self):
        if self.status=='P':
            return False
        return True
    
    # def markAsFulfilled(self):
    #     update field in db
    
    def getStudentName(self):
        student = Student.objects.get(pk=self.student_id)
        user = User.objects.get(pk=student.user)
        if user is not None: 
            return user.first_name , " " , user.last_name 

    # for epic 2
    #additionalInfo = models.TextField(default = "N/A")
