from django.core.exceptions import ValidationError
import datetime
from datetime import datetime, date 
from lessons.models import Term,LessonBooking,LessonRequest
from django.utils.timezone import now



def checkIfDuringTerm():
    #get this term! 
    return Term.objects.filter(start_of_term_date__gte=now, end_of_term_date__lte=now).exists()
       
def getCurrentTerm():
    if checkIfDuringTerm():
        current_term = Term.objects.get(start_of_term_date__gte=now, end_of_term_date__lte=now)
        return current_term 
#For epic 2.2 later need to validate lesson start dates 

#This assumes we are not during a term
def getNearestTerm(input_date):
    #if we are during term then , admin specifies a date
    if not checkIfDuringTerm()  :
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
    return False

    #if lessons start midterm then admin specifies a date
    #otherwise admin just specifies WHAT term the lessons are booked
    #If this is done close to the start of an upcoming term or during the holiday, then the default term is the upcoming term
    #If no end date is given, by default book lessons for rest of term 
    #A schedule is created for these remaining lessons 

def getDateRange(start : datetime, end : datetime):
    for n in range (int((end - start).days)+1):
        yield start + datetime.timedelta(n)

def bookScheduleForNewTerm(term : Term , num_of_lessons , start_date : datetime , end_date : datetime , day_of_week : int , lesson_interval : int): 
    if(start_date is None):
        start_date=term.start_of_term_date
    if(end_date is None):
        end_date = term.end_of_term_date
    found_start = False 
    lessons_scheduled= 0 
    week_count = 0
    date_list = []
    for d in getDateRange(start_date, end_date):
        if d.weekday() == day_of_week and lessons_scheduled<num_of_lessons and week_count%lesson_interval==0 :
            date_list.append(d)
            lessons_scheduled+=1
            week_count+=1 
    return date_list 