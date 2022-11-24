from django.db import models

# Create your models here.

# Aodhán

"""
Template user class to be replaced
"""
class User:
    studentNumber = "0000"
    balence = 0
    pass

"""
A simple class to store a reference number and an amount paid
"""
class BankTransfer:
    amount = 0              # The amount transferred
    studentNumber = "0000"  # The student number used to identify which student is paying, this is 4 digits long
    invoiceNumber = "000"   # The invoice number, this is 3 digits long


    """
    Initialise the BankTransfer with the amount paid, the student's number
    and the invoice number
    """
    def __init__(self, amount, studentNumber, invoiceNumber):
        self.amount = amount
        self.studentNumber = studentNumber
        self.invoiceNumber = invoiceNumber


    """
    Return the full reference number, as a string, constructed from
    seperating the student number from the invoice number by a dash
    """
    def getReferenceNumber(self):
        return f"{self.studentNumber}-{self.invoiceNumber}"


    """
    Return the amount paid
    """
    def getAmount(self):
        return self.amount
    
    def setAmount(self, amount):
        self.amount = amount


"""
Temporary skeleton teacher class, to be replaced
"""
class Teacher:
    cost = 0
    name = ""

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def getCost(self): return self.cost

    def getName(self): return self.name

"""
Temporary skeleton class for bookings
"""
class Booking:
    day = 0                     # Unsure how the project wants us to store the day vs start date of lessons
    teacher = Teacher()         # The teacher assigned
    startDate = 0               # See: day
    lessonDuration = 0          # The duration of each lesson (usually between 30 and 60 minutes)
    lessonInterval = 0          # The number of days or weeks between lessons
    numberOfLessons = 0         # The total number of pre-booked lessons
    invoice = Invoice()         # The invoice associated with the booking

    def __init__(self, stuNum, inNum, day, teacher, startDate, lessonDur, lessonIntrv, numOfLessons):
        self.day = day
        self.teacher = teacher
        self.startDate = startDate
        self.lessonDuration = lessonDur
        self.lessonInterval = lessonIntrv
        self.numberOfLessons = numOfLessons
        price = lessonDur * numOfLessons * teacher.getCost()
        self.invoice = Invoice(price, stuNum, inNum, self)


    def getDay(self): return self.day
        
    def getTeacher(self): return self.teacher

    def getStartDate(self): return self.startDate

    def getLessonDur(self): return self.lessonDuration

    def getLessonIntrv(self): return self.lessonInterval

    def getNumOfLessons(self): return self.numberOfLessons

    def getInvoice(self): return self.invoice

    def setDay(self, day):
        if self.day == day: pass
        self.invoice.updateDay(day)
        self.day = day

    def setTeacher(self, teacher):
        if self.teacher == teacher: pass
        self.invoice.updateTeacher(teacher)
        self.teacher = teacher

    def setStartDate(self, startDate):
        if self.startDate == startDate: pass
        self.invoice.updateStartDate(startDate)
        self.startDate = startDate
        
    def setLessonDur(self, duration):
        if self.lessonDuration == duration: pass
        self.invoice.updateLessonDur(duration)
        self.lessonDuration = duration

    def setLessonInterval(self, interval):
        if self.lessonInterval == interval: pass
        self.invoice.updateLessonIntrv(interval)
        self.lessonInterval = interval

    def setPrice(self, amount):
        if self.invoice.getTransfer().getAmount() == amount: pass
        self.invoice.updateAmount(amount)
    
"""
An invoice
"""
class Invoice:
    transfer = BankTransfer()       # The money being transferred complete with an reference number
    booking = Booking()             # The booking referenced by the invoice

    history = ""                    # A string storing the history of the invoice/booking

    def __init__(self, amount, stuNum, inNum, booking):
        self.transfer = BankTransfer(amount, stuNum, inNum)
        self.booking = booking

        """
        Record the initialisation of the invoice with the initial values
        """
        self.history = f"Invoice created with reference number: {self.transfer.getReferenceNumber()}, for an amount: £{'%.2f' % self.transfer.getAmount()}."
        self.history += f"\nLessons set for {self.booking.getDay()}, starting from {self.booking.getStartDate()}, with {self.booking.getTeacher().getName()} teaching."
        self.history += f"\n{self.booking.getNumOfLessons()} lessons booked with a duration of {self.booking.getLessonDur()} minutes and an interval of {self.booking.getLessonIntrv()}."

    def getTransfer(self): return self.transfer

    def getBooking(self): return self.booking

    def getHistory(self): return self.history


    """
    Whenever the booking or invoice is updated, record those changes in history
    """
    def updateDay(self, day):
        self.history += f"\nLesson day changed from {self.booking.getDay()} to {day}."

    def updateTeacher(self, teacher):
        self.history += f"\nLesson teacher changed from {self.booking.getTeacher().getName()} to {teacher.getName()}."

    def updateStartDate(self, startDate):
        self.history += f"\nLesson start date changed from {self.booking.getStartDate()} to {startDate}."
    
    def updateLessonDur(self, duration):
        self.history += f"\nLesson duration changed from {self.booking.getLessonDur()} minutes to {duration} minutes."

    def updateLessonIntrv(self, interval):
        self.history += f"\nLesson interval changed form {self.booking.getLessonIntrv()} to {interval}."

    def updateAmount(self, amount):
        self.history += f"\nTotal cost changed from £{'%.2f' % self.transfer.getAmount()} to £{'%.2f' % amount}."
        self.transfer.setAmount(amount)


    
# /Aodhán  

        
        

