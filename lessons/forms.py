from django import forms
from .models.requests import request

#student forms

class make_request(forms.ModelForm):

    class Meta:
        model = request
        fields =[

        
       'Teacher',
        'Date',
        'time',
        'durations',
        'lesson_type'

        
        ]
