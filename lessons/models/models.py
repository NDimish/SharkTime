from django.db import models


# Create your models here.
class Student(models.Model):
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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    lesson_num = models.IntegerField(max_length=5)
    lesson_price = models.FloatField(max_length=10)
    interval = models.IntegerField(max_length=3, verbose_name="unit is day")
    duration = models.IntegerField(max_length=5, validators="unit minutes")
    description = models.CharField(max_length=500, null=True)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


class LessonBook(models.Model):
    lesson_id = models.IntegerField(max_length=20)
    lesson_name = models.CharField(max_length=50, null=True)
    book_status = models.IntegerField(max_length=5)
    booking_time = models.DateTimeField(null=False)
    student_id = models.IntegerField(max_length=20)
    remarks = models.CharField(max_length=500, null=True)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


class LessonConfirmed(models.Model):
    lesson_id = models.IntegerField(max_length=20)
    teacher_id = models.IntegerField(max_length=20)
    schedule_time = models.DateTimeField(null=False)
    finish_time = models.DateTimeField(null=False)
    create_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(null=False)


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
