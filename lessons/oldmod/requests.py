# from django.db import models
# from django.utils.timezone import now
# from lessons import helpers
# from .users import Student 
# from .users import User
# from django.utils.translation import gettext as _
# from django.contrib import admin
# from django import forms







# class request(models.Model):

#     REQUEST_BOOK_STATUS_CHOICES = (
#         ('P', 'Pending'),
#         ('R', 'Rejected'),
#         ('A', 'Accepted'),
#         ('O', 'Old'),
#     )

  

#     student_id = models.ForeignKey(to=Student, related_name = 'request', on_delete=models.CASCADE )
#     book_status = models.CharField(max_length=1, blank=False, choices=REQUEST_BOOK_STATUS_CHOICES,default= "O" )
#     lesson_time = models.TimeField(default=now, null=False)
#     lesson_interval = models.IntegerField(blank=False,choices=helpers.CHOICE_LESSON_INTERVAL, default=1 )
#     lesson_duration = models.IntegerField(blank=False, choices=helpers.CHOICE_LESSON_DURATION, default=1)
#     number_of_lessons = models.IntegerField(validators=[helpers.validateLessonNumber])
#     lesson_teacher = models.CharField(max_length = 20, default='')
#     lesson_type = models.CharField(max_length=50, null=True)
#     lesson_start_date = models.DateField(null=False,default = now)
#     date_created = models.DateField(null=False,default = now)
#     remarks = models.CharField(max_length=500, null=True)
#     objects = models.Manager()

#     def isFulfilled(self):
#         if self.book_status=='P':
#             return False
#         return True

#     def getStudentName(self):
#         student = Student.objects.get(pk=self.student_id)
#         user = User.objects.get(pk=student.user)
#         if user is not None: 
#             return user.first_name , " " , user.last_name 

#     # for epic 2
#     #additionalInfo = models.TextField(default = "N/A")
#     LESSON_DURATION_MAX_LENGTH=10
#     LESSON_INTERVAL_MAX_LENGTH=22