from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
#helper file 
from lessons import helpers 
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Studentsss(models.Model):
    reference_number = models.IntegerField(max_length=50, null=False, verbose_name="student id")
    name = models.CharField(max_length=80, null=False, verbose_name="student name")
    age = models.IntegerField(max_length=5, null=False)
    email = models.CharField(max_length=500, null=False, verbose_name="user name or email address")
    nick_name = models.CharField(max_length=500, null=True)
    password = models.CharField(max_length=500, null=True)
    icon_url = models.CharField(max_length=500, null=True)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


class Teacher(models.Model):
    reference_number = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=30, null=True)
    nick_name = models.CharField(max_length=20, null=True)
    special = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=100, null=True)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


class Lesson(models.Model):
    name = models.CharField(max_length=50, null=True)
    lesson_num = models.IntegerField(max_length=5)
    lesson_price = models.FloatField(max_length=10)
    interval = models.IntegerField(max_length=3)
    duration = models.IntegerField(max_length=5)
    description = models.CharField(max_length=500, null=True)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)



    CHOICE_LESSON_DURATION = (
        (3, 60),
        (1, 30),
        (2, 45),
    )


class LessonBook(models.Model):

    request_status = (
        ('P', 'Pending'),
        ('R', 'Rejected'),
        ('A', 'Accepted'),
        ('O', 'Old'),
    )


    CHOICE_LESSON_DURATION = (
        (3, 60),
        (1, 30),
        (2, 45),
    )


    lesson_type = models.CharField(max_length=50, null=True)
    book_status = models.CharField(max_length=1, blank=False, choices=request_status,default= "O" )
    booking_time = models.TimeField(null=False)
    student_id = models.IntegerField(max_length=20)
    remarks = models.CharField(max_length=500, null=True)
    book_duration = models.IntegerField(max_length=1, blank=False, choices=CHOICE_LESSON_DURATION,default= '1' )
    create_time = models.DateField(null=False,default=now)
    book_date = models.DateField(null=False)
    objects = models.Manager()

    def isFulfilled(self):
        if(self.book_status=='A'):
            return True
        return False

    def markAsFulfilled(self):
        self.book_status = 'A' 

LESSON_DURATION_MAX_LENGTH=10
LESSON_INTERVAL_MAX_LENGTH=22
class LessonConfirmed(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.ForeignKey(to=LessonBook , related_name = 'bookings', on_delete=models.CASCADE )
    lesson_id = models.IntegerField(max_length=20)
    teacher_id = models.IntegerField(max_length=20)
    time_of_lesson = models.DecimalField(decimal_places = 2, max_digits= 4)
    finish_time = models.DateTimeField(null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=False)
    start_date = models.DateField(validators=[helpers.validateDate]) 
    CHOICE_LESSON_DURATION = (
        (3, 60),
        (1, 30),
        (2, 45),
    )
    CHOICE_LESSON_INTERVAL = ((1, '1 lesson every week'), (2, '1 lesson every 2 weeks'))
    lesson_duration = models.IntegerField(choices=CHOICE_LESSON_DURATION,default=1,blank=False)
    lesson_interval = models.IntegerField(choices=CHOICE_LESSON_INTERVAL,default=1,blank=False)

    number_of_lessons = models.IntegerField(validators=[helpers.validateLessonNumber])
    objects = models.Manager() 









class Payment(models.Model):
    customer_id = models.IntegerField(max_length=20)
    staff_id = models.IntegerField(max_length=20)
    amount = models.FloatField(null=False, max_length=20)
    payment_date = models.DateTimeField(null=False)
    payment_type = models.IntegerField(max_length=5, null=False)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


class Sys_user(models.Model):
    """User account"""
    # INSERT INTO `sys_user`(`id`, `username`, `password`, `salt`, `name`, `create_time`, `create_by`, `update_time`,
    # `update_by`) VALUES(1, 'admin', 'admin', '123456', 'super administrator', DEFAULT, NULL, DEFAULT, NULL)
    user_name = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)
    salt = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


class Sys_authority(models.Model):
    """Role Table"""
    label = models.CharField(max_length=20, null=True, verbose_name="Role Name")
    alias = models.CharField(max_length=20, null=True, verbose_name="Role Alias")
    sort = models.IntegerField(max_length=5, null=False, verbose_name="sort", default=0)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


class Sys_user_authority(models.Model):
    """User Role Table"""
    user_id = models.IntegerField(max_length=20)
    authority_id = models.IntegerField(max_length=20)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)
