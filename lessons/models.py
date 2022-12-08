from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin
from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import UserManager
import uuid 
import random


#helper file 
from lessons import helpers 
from django.utils.translation import gettext_lazy as _

LESSON_DURATION_MAX_LENGTH=10
LESSON_INTERVAL_MAX_LENGTH=22

def random_id():
    return str(random.randint(1111,9999))
#The User model 
class User(AbstractUser):
    USER_ROLES = (
        ('A', 'Administrator'),
        ('D', 'Director'),
        ('S', 'Student'),
    )

    role = models.CharField(max_length=1, blank=False, choices=USER_ROLES )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100,null=False, verbose_name="user name or email address", unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
   
    def __str__(self):
        return '{}'.format(self.get_full_name())

#Student class 
class Student(models.Model):
    #unique student_id 
    id = models.AutoField(primary_key=True)
    #unique 4 digit student reference number
    reference_number =models.CharField(default = random_id, max_length=4, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    nick_name = models.CharField(max_length=500, null=True)
    age = models.IntegerField(null=False)
    objects = models.Manager()
    dependent_id = models.IntegerField(null=True)
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['reference_number'], name='unique_migration_refno_combination'
    #         )
    # ]


    def __str__(self):
        return (self.user.first_name + " " + self.user.last_name + " ID ("  + str(self.id) + ")" + "reference_number = " + self.reference_number)  
    


#Admin class
class Administrator(models.Model):
    #unique admin id 
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

#Director class 
class Director(models.Model):
    #unique admin id 
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField( max_length=30, null=True)
    CHOICE_TITLE = ((1, "MRS") , (2, "MR") , (3,"MISS") , (4,"MS"))

    CHOICE_LESSON_DURATION = (
        (3, 60),
        (1, 30),
        (2, 45),
    )
    reference_number = models.CharField(max_length=50, null=False)
    title = models.IntegerField(choices=CHOICE_TITLE,default=1,blank=False)
    name = models.CharField(max_length=50, null=True)
    speciality = models.CharField(max_length=10, null=True)
    objects = models.Manager()
    



class Payment(models.Model):
    customer_id = models.IntegerField()
    staff_id = models.IntegerField()
    amount = models.FloatField(null=False)
    payment_date = models.DateTimeField(null=False)
    payment_type = models.IntegerField( null=False)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


class Sys_user(models.Model):
    """User account"""
    # INSERT INTO `sys_user`(`id`, `username`, `password`, `salt`, `name`, `create_time`, `create_by`, `update_time`,
    # `update_by`) VALUES(1, 'admin', 'admin', '123456', 'super administrator', DEFAULT, NULL, DEFAULT, NULL)
    user_name = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    password = models.CharField(max_length=20, null=True)
    salt = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)

class Sys_authority(models.Model):
    """Role Table"""
    label = models.CharField(max_length=20, null=True, verbose_name="Role Name")
    alias = models.CharField(max_length=20, null=True, verbose_name="Role Alias")
    sort = models.IntegerField( null=False, verbose_name="sort", default=0)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


class Sys_user_authority(models.Model):
    """User Role Table"""
    user_id = models.IntegerField()
    authority_id = models.IntegerField()
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)

class Lesson(models.Model):
    name = models.CharField(max_length=50, null=True)
    lesson_price = models.FloatField()
    duration = models.IntegerField()
    description = models.CharField(max_length=500, null=True)
    objects = models.Manager()

    CHOICE_LESSON_DURATION = (
        (3, 60),
        (1, 30),
        (2, 45),
    )



class LessonRequest(models.Model):
    
    REQUEST_BOOK_STATUS_CHOICES = (
        ('P', 'Pending'),
        ('R', 'Rejected'),
        ('A', 'Accepted'),
        ('O', 'Old'),
    )

    student_id = models.ForeignKey(to=Student, related_name = 'request', on_delete=models.CASCADE )
    book_status = models.CharField(max_length=1, blank=False, choices=REQUEST_BOOK_STATUS_CHOICES,default= "P" )
    lesson_time = models.TimeField( null=False)
    lesson_interval = models.IntegerField(blank=False,choices=helpers.CHOICE_LESSON_INTERVAL, default=1 )
    lesson_duration = models.IntegerField(blank=False, choices=helpers.CHOICE_LESSON_DURATION, default=1)
    number_of_lessons = models.IntegerField(validators=[helpers.validateLessonNumber])
    submit_depend_id = models.ForeignKey(to=Student, related_name='request_commit', on_delete=models.CASCADE)
    lesson_teacher = models.ForeignKey(to=Teacher, related_name = 'Teaching', on_delete=models.CASCADE )
    lesson_type = models.ForeignKey(to=Lesson, related_name = 'Lessontype', on_delete=models.CASCADE )
    lesson_start_date = models.DateField(null=True,default = now)
    date_created = models.DateField(null=False,default = now)
    remarks = models.CharField(max_length=500, null=True)
    lesson_day_of_week = models.IntegerField(blank = False , choices=helpers.CHOICE_DAY_OF_THE_WEEK )
    objects = models.Manager()

    def isFulfilled(self):
        if self.book_status=='A':
            return True
    def isRejected(self):
        if self.book_status=="R":
            return True 
      

    @property
    def getStudentName(self):
        obj = self.student_id
        user = obj.user
        return str(user)
        
        
        # .first_name.removeprefix('"')
        # return  ( first_name, " " , obj.user.last_name)
         

    # for epic 2
    #additionalInfo = models.TextField(default = "N/A")
    

class Term(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null = False)
    start_of_term_date = models.DateField(null=False,default = now)
    end_of_term_date =  models.DateField(null=False,default = now)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager() 
    def __str__(self):
        return self.name 




    
class LessonBooking(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.ForeignKey(to=LessonRequest , related_name = 'LessonBookings', on_delete=models.CASCADE )
    #lesson_id = models.IntegerField(max_length=20)
    teacher_id = models.IntegerField(null=False, default=1)
    lesson_time = models.TimeField(null=False)
    finish_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lesson_start_date = models.DateField(validators=[helpers.validateDate]) 
    lesson_end_date = models.DateField(validators=[helpers.validateDate]) 
    CHOICE_LESSON_DURATION = (
        (3, 60),
        (1, 30),
        (2, 45),
    )
    CHOICE_LESSON_INTERVAL = ((1, '1 lesson every week'), (2, '1 lesson every 2 weeks'))
    lesson_duration = models.IntegerField(choices=CHOICE_LESSON_DURATION,default=1,blank=False)
    lesson_interval = models.IntegerField(choices=CHOICE_LESSON_INTERVAL,default=1,blank=False)
    lesson_type = models.CharField(max_length=50, null=True)
    number_of_lessons = models.IntegerField(validators=[helpers.validateLessonNumber])
    lesson_day_of_week = models.IntegerField(blank = False , choices=helpers.CHOICE_DAY_OF_THE_WEEK )
    lesson_teacher = models.CharField(max_length = 20, default='')
    objects = models.Manager()
