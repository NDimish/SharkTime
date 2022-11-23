from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def userDetails(request):
    return render(request,'studentHome.html',{'name': None})


def button(request):
    return"hello"



#@app.route('/my-link/')
#def my_link():
   #  return 'Click.'