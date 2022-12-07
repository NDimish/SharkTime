from django.core.exceptions import ValidationError
import datetime
from datetime import datetime 
import datetime as dt
from lessons.models import Term,LessonBooking,LessonRequest, Student, User


FORMAT = "%Y-%m-%d"

def checkIfDuringTerm():
    #get this term! 
    now = dt.datetime.now()
    now = datetime.strftime(now, FORMAT)

    return Term.objects.filter(start_of_term_date__gte=now, end_of_term_date__lte=now).exists()

def checkIfDateDuringTerm(d):
    if isinstance(d, str) : 
        d = datetime.strptime(d, FORMAT)
    return Term.objects.filter(start_of_term_date__gte=d, end_of_term_date__lte=d).exists()
def getCurrentTerm():
    if checkIfDuringTerm():
        current_term = Term.objects.get(start_of_term_date__gte=now, end_of_term_date__lte=now)
        return current_term 

def getCurrentTermFromDate(d):
    if isinstance(d, str) : 
        d = datetime.strptime(d, FORMAT)
    current_term = Term.objects.get(start_of_term_date__gte=d, end_of_term_date__lte=d)
    return current_term 

#This assumes we are not during a term
def getNearestTerm(input_date):
    #if we are during term then , admin specifies a date
    if not checkIfDuringTerm()  :
        now = dt.datetime.now().date()
       # now = datetime.strftime(now, FORMAT)

        #Order the data so that the first object is closest to the current date
        term_list = Term.objects.filter(start_of_term_date__gte=now).order_by('start_of_term_date')
        nearest_upcoming_term = None
        for term in term_list:
            #Term must be UPCOMING
            if term.start_of_term_date > now :
                nearest_upcoming_term=term
                break
        #check if a term date was found
        if nearest_upcoming_term is not None:
            return nearest_upcoming_term
    return None

    #if lessons start midterm then admin specifies a date
    #otherwise admin just specifies WHAT term the lessons are booked
    #If this is done close to the start of an upcoming term or during the holiday, then the default term is the upcoming term
    #If no end date is given, by default book lessons for rest of term 
    #A schedule is created for these remaining lessons 

def getDateRange(start , end ):
    list = []
    if isinstance(start,str):
        start = datetime.strptime(start, FORMAT)
    if isinstance(end,str):
        end = datetime.strptime(end, FORMAT)
    # end = end.date()
    for n in range (int((end - start).days)+1):
      
        list.append(start + dt.timedelta(n))
    return list

def getDateListOfScheduleForNewTerm(term : Term , num_of_lessons , start_date : datetime , end_date : datetime , day_of_week : int , lesson_interval : int): 
    day_of_week = int(day_of_week)
    lesson_interval = int(lesson_interval)
    num_of_lessons = int(num_of_lessons)
    if term is not None : 
        if(start_date is None):
            start_date=term.start_of_term_date
        #if(end_date is None):
        end_date = term.end_of_term_date

    lessons_scheduled= 0 
    week_count = 1
    date_list = []
    list = []

    list = getDateRange(start_date,end_date)
    for d in list:
  
        if d.weekday()== day_of_week and lessons_scheduled<num_of_lessons and (lesson_interval-1)%week_count==0 :
            date_list.append(d)
            print("date is " , d)
            lessons_scheduled+=1
            week_count+=1 
    return date_list 

#Given a booking object , a schedule can be generated from it 
def getDateListGivenASchedule(num_of_lessons,  start_date : datetime , end_date : datetime , day_of_week : int , lesson_interval : int): 
    day_of_week = int(day_of_week)
    lesson_interval = int(lesson_interval)
    num_of_lessons = int(num_of_lessons)

    lessons_scheduled= 0 
    week_count = 1
    date_list = []
    list = []

    list = getDateRange(start_date,end_date)
    for d in list:
  
        if d.weekday()== day_of_week and lessons_scheduled<num_of_lessons and (lesson_interval-1)%week_count==0 :
            date_list.append(d)
            print("date is " , d)
            lessons_scheduled+=1
            week_count+=1 
    return date_list

#given a request id , get the name of the student
def getStudentName(id):
    #Get the request
    req = LessonRequest.objects.get(pk=id)
    #Get the student
    student = Student.objects.get(pk=req.student_id)
    #get the user
    user = User.objects.get(user)
    return user.first_name ,  " " , user.last_name 