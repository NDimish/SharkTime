from django.contrib import admin
from .models.requests import request
from .models import User
# Register your models here.
admin.site.register(request)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=[
    'first_name','last_name','email',
    ]
