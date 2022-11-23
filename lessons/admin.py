from django.contrib import admin

# Register your models here.

# Aodhán
from .models import User

"""
Skeleton template admin class to be replaced
"""
@admin.register(User)
class MusicAdmin(admin.ModelAdmin):
    
    """
    Arbitrary skeleton method for confirming a student's lesson request
    """
    def confirm(self, request, day, teacher, start, duration, interval, number):
        request.set(day, teacher, start, duration, interval, number)
        booking = request.makeBooking()
        database.addBooking(booking)
        price = duration * number * teacher.getCost()
        database.addInvoice(booking, price)



# /Aodhán