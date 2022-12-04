from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.utils.timezone import now
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from ..forms.studentforms import make_request
from ..models.requests import request as database

# Create your views here.
def studentHomePage(request):

    obj =  database.objects.filter(Student = "testbob")
    
    data ={
        'name' :'nathan',
        'Available_lessons' : [1,2,3,45,5,6,76,2,3,4,56,7,34,345,345,57,56634,54,5765,75,]
    
    }


    return render(request,'studentHome.html',data)




def studentViewRequests(request):
    obj =  database.objects.filter(Student = "testbob")
    Pending = database.objects.filter(Student = "testbob", status ="P")
    for book in Pending:
        if(now().date().today() > book.Date):
            book.status = "R"
            book.save()
       


    Pending = database.objects.filter(Student = "testbob", status ="P")

    Rejected = database.objects.filter(Student = "testbob", status ="R")
    Approved = database.objects.filter(Student = "testbob", status ="A")
    
    data ={

        'booked_lessons' : obj,
        'Pending_lessons':Pending,
        'Rejected_lessons':Rejected,
        'Accepted_lessons':Approved,
    
    }


    return render(request,'studentViewRequests.html',data)    


def studentViewInvoices(request):
    data = {
        'Invoices' : database.objects.filter(Student = "testbob", status ="A")
    }

    return render(request,'studentViewInvoices.html',data)


def makeAndViewInvoice(request, my_id):
    # Grab the student
    student = database.objects.get(id=my_id)
    
    # Creat a buffer for receiving PDF data and intialise a pdf to save onto it
    pdfBuffer = io.BytesIO()

    pdf = canvas.Canvas(pdfBuffer)

    # Let's add stuff!
    pdf.drawString(10, 10, "Oi Oi guv'nor.")
    # This currently creates a PDF with the above text displayed in the lower left hand corner

    # render, save, close
    pdf.showPage()
    pdf.save()

    # Grab the pdf from the buffer to export
    pdfBuffer.seek(0)

    return FileResponse(pdfBuffer, as_attachment=True, filename=f'invoice-{my_id}.pdf')



def studentMakeRequest(request):

    form = make_request(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('studentVeiwRequests'))
    data ={
        'form':form
    
    }


    return render(request,'request.html',data)



def studentEditRequest(request,my_id):

    try:
        obj = get_object_or_404(database,id=my_id)
    except database.DoesNotExist:
        raise Http404
    if(obj.status != "P"):
        return HttpResponseRedirect(reverse('studentHome'))

    context ={
        'Teacher': obj.Teacher,
        'Date': obj.Date,
        'time': obj.time,
        'durations': obj.duration,
        'lesson_type':obj.lesson_type,
        }
    form = make_request(request.POST or None, initial = context)

   

    data ={
        'data':obj,
        'form':form

    }
    

    return render(request,'editrequest.html', data)


def Editrecord(request,my_id):
    if("Edit" in request.POST):
        return update(request,my_id)
    elif("Delete" in request.POST):
        return delete(request, my_id)
    else:
        #change later
        return HttpResponseRedirect(reverse('studentHome'))


def update(request,my_id):
    member = database.objects.get(id=my_id)

    member.Teacher = request.POST['Teacher']
    member.Date = request.POST['Date']
    member.Time = request.POST['time']
    member.durations = request.POST['durations']
    member.lesson_type = request.POST['lesson_type']

    member.save()
    return HttpResponseRedirect(reverse('studentVeiwRequests'))



def delete(request, my_id):
  member = database.objects.get(id=my_id)
  member.delete()
  return HttpResponseRedirect(reverse('studentVeiwRequests'))



#function


#get requests for user

    

#get pending requests

# edit pending requests

# check if valid
#check terms in type
#

