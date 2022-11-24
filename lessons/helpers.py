#Add helper functions here - includes validators 
from django.core.exceptions import ValidationError
import datetime 

DAY_OF_THE_WEEK = {
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    #For now, assume weekend leesons are not possible to book 
    #(5, 'Saturday'),
    #(6, 'Sunday'),
}

LESSON_DURATIONS =  {

}
#VALIDATORS--------------------------------------

# Reject dates in the past  
def validateDate(date):
    if date<datetime.date.today():
        raise ValidationError("Date cannot be in the past")

# Validate the number of lessons 
def validateLessonNumber(lessonNum):
    #For now assume a maximum of 10 lessons can be booked
    if (lessonNum<1 or lessonNum>10):
        raise ValidationError("Invalid number of lessons")


#For epic 2.2 later need to validate lesson start dates 