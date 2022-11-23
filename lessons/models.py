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

# /Aodhán  

        
        

