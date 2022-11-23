from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def studentHomePage(request):
    data ={
        'name' :'nathan',
        'booked_lessons' :[0,2,3,4,5,6]
    
    }


    return render(request,'studentHome.html',data)


def button(request):
    return"hello"




#function


#get requests for user

#get pending requests

# edit pending requests

# check if valid
#check terms in type
#

