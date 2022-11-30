from django.db import models
from models import bookings

"""
A simple class to store a reference number and an amount paid
"""
class bankTransfer:
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

    def getAmount(self):
        return self.amount
    
    def setAmount(self, amount):
        self.amount = amount


"""
An invoice
"""
class invoice:
    transfer = bankTransfer()       # The money being transferred complete with an reference number
    booking = booking()             # The booking referenced by the invoice

    history = ""                    # A string storing the history of the invoice/booking

    def __init__(self, amount, stuNum, inNum, booking):
        self.transfer = bankTransfer(amount, stuNum, inNum)
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


