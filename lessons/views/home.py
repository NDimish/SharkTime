from django.shortcuts import render
from django.http import HttpResponse
#default view 
def home(request):
    return render(request,'home.html')