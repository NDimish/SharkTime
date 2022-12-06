from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from ..forms.studentforms import make_request
from lessons.models import LessonRequest as database
from django.urls import reverse
from django.utils.timezone import now
from lessons.models import User, Student, Lesson
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def studentHomePage(request,Logged_ID):
    obj = User.objects.filter(id = Logged_ID).first()
    data = {
        'name' : obj.first_name , 
        'Available_lessons' : [23,3,4,4,2],
        'Logged_ID':Logged_ID
    }

    return render(request,'studentHome.html',data)

@login_required
def studentViewRequests(request,Logged_ID):
    obj = database.objects.all()
    #For now just get the first student in the database
    #student = User.objects.filter(role='S').first()
    student = Student.objects.first()
    print(student.pk, "says hello")
    s = student.pk
    print("student id is " , obj)
    Pending = database.objects.filter( book_status ="P")
    for book in Pending:
        if(now().date().today() > book.lesson_start_date):
            book.book_status = "R"
            #book.save()



    Pending = database.objects.filter(student_id= s, book_status ="P")

    Rejected = database.objects.filter(student_id= s, book_status ="R")
    Approved = database.objects.filter(student_id= s, book_status ="A")

    data ={
        'booked_lessons' : obj,
        'Pending_lessons':Pending,
        'Rejected_lessons':Rejected,
        'Accepted_lessons':Approved,
        'Logged_ID':Logged_ID,
    
    }


    return render(request,'studentViewRequests.html',data)


def makeAndViewInvoice(request, my_id):
    lesson = get_object_or_404(database,id=my_id)
    
    # Creat a buffer for receiving PDF data and intialise a pdf to save onto it
    pdfBuffer = io.BytesIO()

    pdf = canvas.Canvas(pdfBuffer, pagesize=A4)

    # Set font and fontsize
    pdf.setFont("Courier-Bold", 36)

    # Move the origin of the document to the given coords (by default it is lower left corner)
    pdf.translate(30,800)

    # Let's add stuff!
    pdf.setTitle("Invoice")

    pdf.drawString(0, 0, "INVOICE")
 
    pdf.setFont("Helvetica-Bold", 14)
    x = -40
    pdf.drawString(0, x, "Shark Time Music School")
    # If multiple schools are implemented then make this variable
    pdf.setFont("Helvetica", 14)
    pdf.drawString(0, x - 22, "47 Haberdashery Avenue")
    pdf.drawString(0, x - 42, "London, W2 1DS")
    
    y = x - 90
    pdf.drawString(0, y, f"{lesson.Student}")

    pdf.setFont("Courier-Bold", 18)
    pdf.drawString(0, y + 20, "BILL TO")
    
    v = 270
    pdf.drawString(v, y + 40, "INVOICE #")
    pdf.drawString(v, y + 20, "INVOICE DATE")
    pdf.drawString(v, y, "DUE DATE")

    z = y - 30
    pdf.line(-100, z + 15, 1000, z + 15)
    pdf.drawString(0, z, "QTY")
    pdf.drawString(50, z, "DESC")
    pdf.drawString(400, z, "AMOUNT")
    pdf.line(-100, z - 5, 1000, z - 5)

    w = z - 20

    pdf.drawString(330, w - 100, "TOTAL")
    pdf.drawString(400, w - 100, f"£{'{:.2f}'.format(30)}")


    pdf.setFont("Helvetica", 10)
    pdf.drawString(12, w, "1")
    # Get the values from the lesson booking and display them on the invoice
    pdf.drawString(50, w, f"{lesson.duration[int(lesson.durations) - 1][1]} minute {lesson.lesson_type} lesson taught by {lesson.Teacher} on {lesson.Date}.")
    pdf.drawString(400, w, f"£{'{:.2f}'.format(30)}")

    pdf.drawString(v + 160, y + 40, f"{'%04d' % my_id}")
    # Replace this with student id + invoice id
    pdf.drawString(v + 160, y + 20, f"{lesson.DateSent}")
    # Replace this with whenever the request was accepted
    from datetime import timedelta
    pdf.drawString(v + 160, y, f"{lesson.DateSent + timedelta(days=30)}")

    a = -730
    b = 240
    pdf.setFont("Courier-Bold", 14)
    pdf.drawString(b, a, "TERMS & CONDITIONS")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(b, a - 20, "Payment is due within 30 days.")
    pdf.drawString(b, a - 35, "Please make checks payable to: Shark Time Music School")
    pdf.line(b - 5, a + 10, b - 5, a - 50)

    # render, save, close
    pdf.showPage()
    pdf.save()

    # Grab the PDF from the buffer to export
    pdfBuffer.seek(0)

    return FileResponse(pdfBuffer, as_attachment=False, filename=f'invoice-{"%04d" % my_id}.pdf')
    # as_attachment determines (primarily) whether the PDF will be downloaded automatically


def studentMakeRequest(request):

    form = make_request(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse('studentViewRequests') ,Logged_ID = Logged_ID)
    data ={
        'form':form,
        'Logged_ID':Logged_ID

    }
    return render(request,'request.html',data)

    
@login_required
def studentEditRequest(request,Logged_ID,my_id):
    try:
        obj = get_object_or_404(database,id=my_id)
    except database.DoesNotExist:
        raise Http404
    if(obj.book_status != "P"):
        return HttpResponseRedirect(reverse('studentHome'), Logged_ID = Logged_ID)

    context ={
        'lesson_teacher': obj.lesson_teacher,
        'lesson_start_date': obj.lesson_start_date,
        'lesson_time': obj.lesson_time,
        'lesson_duration': obj.lesson_duration,
        'lesson_type':obj.lesson_type,
        'number_of_lessons':obj.number_of_lessons,
        'student_id':obj.student_id,
        'Logged_ID':Logged_ID
        }
    form = make_request(request.POST or None, initial = context)
   
    data ={
        'data':obj,
        'form':form,
        'Logged_ID':Logged_ID
    }
    
    return render(request,'editrequest.html', data)

@login_required
def Editrecord(request,Logged_ID,my_id):
    if("Edit" in request.POST):
        return update(request,my_id)
    elif("Delete" in request.POST):
        return delete(request, my_id)
    else:
        #change later
        return HttpResponseRedirect(reverse('studentHome'),Logged_ID = Logged_ID)




@login_required
def update(request,Logged_ID,my_id):
    member = database.objects.get(id=my_id)
    member.lesson_teacher = request.POST['lesson_teacher']
    member.lesson_start_date = request.POST['lesson_start_date']
    member.lesson_time = request.POST['lesson_time']
    member.lesson_duration = request.POST['lesson_duration']
    member.lesson_type = request.POST['lesson_type']
    member.number_of_lessons = request.POST['number_of_lessons']

    member.save()
    return HttpResponseRedirect(reverse('studentViewRequests'),Logged_ID = Logged_ID)


    
@login_required
def delete(request,Logged_ID, my_id):
  member = database.objects.get(id=my_id)
  member.delete()
  return HttpResponseRedirect(reverse('studentViewRequests'),Logged_ID = Logged_ID)



