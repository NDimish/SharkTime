from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def studentHomePage(request):
    data ={
        'name' :'nathan',
        'booked_lessons' :'0'
    
    }

    
    return render(request,'studentHome.html',data)


def button(request):
    return"hello"



#@app.route('/my-link/')
#def my_link():
   #  return 'Click.'