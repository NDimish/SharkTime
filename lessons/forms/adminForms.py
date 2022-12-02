from django import forms
from ..models.requests import request
from ..models.bookings import booking 
from ..models import bookings

class bookingForm(forms.ModelForm):

        
    class Meta:
        model = booking
        def __init__(self,  *args, **kwargs):
            self.order_fields(self.Meta.fields)
        #     super(bookingForm, self).__init__(*args, **kwargs)    
        #     qs = request.objects.filter(request=user)
        #     self.fields['account'] = forms.Select(queryset=qs)
       
                # for day in request.availability:
                #     print (str(day))
                #     self.fields['day_of_week'] = forms.Select(day)
       
        #day_of_week = forms.ModelChoiceField(queryset=requests.Weekday.objects.all(),widget=forms.CheckboxSelectMultiple)
        fields = {  'request' , 'lesson_time', 'lesson_type', 'lesson_teacher','lesson_start_date','lesson_duration','lesson_interval','number_of_lessons'}
        labels = {
            
            'lesson_time' : 'Time of Lesson' , 
            'teacher' : 'Teacher' , 
            'lesson_start_date' : 'Start Date' , 
            'lesson_duration' : 'Lesson Duration',
            'lesson_interval' : 'Lesson Interval' , 
            'number_of_lessons' : 'Number Of Lessons' ,
            'day_of_week' : 'Day Of Lesson' , 
            'lesson_type' : 'Lesson Type'
          
        } 
    
        #widget
        widgets = {
            'request' : forms.HiddenInput(), 
            #'created_at' : forms.DateTimeInput(attrs={'class' : 'form-control'}),
            #'updated_at' : forms.DateTimeInput(attrs={'class' : 'form-control'}),
            #'day_of_week' : forms.CheckboxInput(attrs={'class' : 'form-control'}),
            'lesson_time' : forms.TimeInput(attrs={'class' : 'form-control'}),
            'lesson_teacher' : forms.TextInput(attrs={'class' : 'form-control'}),
            'lesson_start_date' : forms.SelectDateWidget(attrs={'class' : 'form-control'}),
            'lesson_duration' : forms.Select(attrs={'class' : 'form-control'}),
            'lesson_interval' : forms.Select(attrs={'class' : 'form-control'}),
            'number_of_lessons' : forms.NumberInput(attrs={'class' : 'form-control'}),
            #'day_of_week' : forms.CheckboxSelectMultiple(attrs={'class' : 'form-control'})
            'lesson_type' : forms.TextInput(attrs={'class' : 'form-control'})
        }   

        #OVERRIDE SAVE METHOD
        def save(self, commit=True):
            """Create a new user."""
            instance = forms.ModelForm.save(self,False)
            
            old_save_m2m = self.save_m2m
            # def save_m2m():
            #     old_save_m2m()
            #     instance.day_of_week.clear()
            #     instance.day_of_week.add(*self.cleaned_data['day_of_week'])
            # self.save_m2m = save_m2m
        
            # self.cleaned_data.get('username'),
            instance.lesson_start_date = self.cleaned_data['lesson_start_date']
            instance.lesson_teacher=self.cleaned_data['lesson_teacher']
            instance.student_id = self.cleaned_data['student_id']
            instance.Date = self.cleaned_data.get('Date')
            instance.lesson_duration = self.cleaned_data['lesson_duration']
            instance.lesson_interval = self.cleaned_data['lesson_interval']
            instance.lesson_type = self.cleaned_data['lesson_type']
            instance.number_of_lessons = self.cleaned_data['number_of_lessons']
            instance.lesson_type = self.cleaned_data['lesson_type']
            
            
            if commit:
                instance.save()
                self.save_m2m()
            
            return instance
        
    
   