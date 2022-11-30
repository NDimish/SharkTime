from django.contrib import admin
from .models.requests import request
from .models.bookings import booking
# Register your models here.
admin.site.register(request)
admin.site.register(booking)