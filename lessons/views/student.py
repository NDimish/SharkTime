from django.shortcuts import render
from django.http import HttpResponse

from ..forms import make_request

# Create your views here.
def studentHomePage(request):

    obj = get_requests()
    data ={
        'name' :'nathan',
        'booked_lessons' :[0,2,3,4,5,6]
    
    }


    return render(request,'studentHome.html',data)



def studentMakeRequest(request):

    form = make_request(request.POST or None)
    if form.is_valid():
        form.save()
    data ={
        'form':form
    
    }


    return render(request,'request.html',data)

def studenEditRequest(request,id):

    form = make_request(request.POST or None)
    

    return render(request,'request.html',)






#function


#get requests for user
def get_requests():
    return 1
    

#get pending requests

# edit pending requests

# check if valid
#check terms in type
#

