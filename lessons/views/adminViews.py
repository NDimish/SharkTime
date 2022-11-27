#contains the views of the admin 
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
import lessons.models as models


"""
    Admin home view - This is the view displayed to the admin after logging in
    - Should display all student requests

"""
def admin_home(request):
    #Get all requests 
    requests = models.request.objects.all()
    #request_count = models.request.objects.all().count()
    return render(request, 'adminHome.html', {'requests' : requests})



    
def admin_view_students(request):
    return render(request, 'adminViewStudents.html')

def view_request(request,id):
    #get the request from db with same pk as selected request
    request = models.request.objects.get(pk=id)
    return HttpResponseRedirect(reverse ('adminHome.html'))