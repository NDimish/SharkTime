from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Director)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Payment)
admin.site.register(Sys_user)
admin.site.register(Sys_user_authority)
admin.site.register(Sys_authority)
admin.site.register(Lesson)
admin.site.register(LessonRequest)
admin.site.register(LessonBooking)





