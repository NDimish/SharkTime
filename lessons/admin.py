from django.contrib import admin
from .models.requests import request
from .models.bookings import booking

from .models import requests
from .models import users
# Register your models here.
admin.site.register(request , requests.requestAdmin)
admin.site.register(booking)
admin.site.register(users.User)
admin.site.register(users.Student)






