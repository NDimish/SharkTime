from django import forms
from ..models.requests import request
from ..models.bookings import booking 

class bookingForm(forms.ModelForm):
   
    class Meta:
        model = booking
        
        fields = {  'request' , 'day_of_week', 'time_of_lesson','teacher','start_date','lesson_duration','lesson_interval','number_of_lessons'}
        labels = {
            'day_of_week' : 'Day Of Lesson' , 
            'time_of_lesson' : 'Time of Lesson' , 
            'teacher' : 'Teacher' , 
            'start_date' : 'Start Date' , 
            'lesson_duration' : 'Lesson Duration',
            'lesson_interval' : 'Lesson Interval' , 
            'number_of_lessons' : 'Number Of Lessons' 
          
        } 
    
        #widget
        widgets = {
            'request' : forms.HiddenInput(), 
            #'created_at' : forms.DateTimeInput(attrs={'class' : 'form-control'}),
            #'updated_at' : forms.DateTimeInput(attrs={'class' : 'form-control'}),
            'day_of_week' : forms.Select(attrs={'class' : 'form-control'}),
            'time_of_lesson' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'teacher' : forms.TextInput(attrs={'class' : 'form-control'}),
            'start_date' : forms.SelectDateWidget(attrs={'class' : 'form-control'}),
            'lesson_duration' : forms.Select(attrs={'class' : 'form-control'}),
            'lesson_interval' : forms.Select(attrs={'class' : 'form-control'}),
            'number_of_lessons' : forms.NumberInput(attrs={'class' : 'form-control'})
        }
        
    
   