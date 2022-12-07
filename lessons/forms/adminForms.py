from django import forms
from django.forms import ValidationError
from lessons.models import LessonRequest
from lessons.models import LessonBooking,Term


class bookingForm(forms.ModelForm):

        
    class Meta:
        model = LessonBooking
   
        fields = {  'request' , 'lesson_time', 'lesson_type', 'lesson_teacher','lesson_start_date','lesson_end_date', 'lesson_duration','lesson_interval', 'lesson_day_of_week','number_of_lessons'}
        labels = {
            
            'lesson_time' : 'Time of Lesson' , 
            'teacher' : 'Teacher' , 
            'lesson_start_date' : 'Start Date' , 
            'lesson_end_date' : 'End Date' , 
            'lesson_duration' : 'Lesson Duration',
            'lesson_interval' : 'Lesson Interval' , 
            'lesson_day_of_week' : 'Day of Lesson',
            'number_of_lessons' : 'Number Of Lessons' , 
            'lesson_type' : 'Lesson Type',
           
          
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
            'lesson_end_date' : forms.SelectDateWidget(attrs={'class' : 'form-control'}),
            'lesson_duration' : forms.Select(attrs={'class' : 'form-control'}),
            'lesson_interval' : forms.Select(attrs={'class' : 'form-control'}),
            'lesson_day_of_week' : forms.Select(attrs={'class' : 'form-control'}),
            'number_of_lessons' : forms.NumberInput(attrs={'class' : 'form-control'}),
            #'day_of_week' : forms.CheckboxSelectMultiple(attrs={'class' : 'form-control'})
            'lesson_type' : forms.TextInput(attrs={'class' : 'form-control'}),

           }

        #OVERRIDE SAVE METHOD
        def save(self, commit=True):
            """Create a new user."""
            instance = forms.ModelForm.save(self,False)
            instance.lesson_start_date = self.cleaned_data['lesson_start_date']
            instance.lesson_end_date = self.cleaned_data['lesson_end_date']
            instance.lesson_teacher=self.cleaned_data['lesson_teacher']
            instance.student_id = self.cleaned_data['student_id']
            instance.Date = self.cleaned_data.get('Date')
            instance.lesson_duration = self.cleaned_data['lesson_duration']
            instance.lesson_interval = self.cleaned_data['lesson_interval']
            instance.lesson_day_of_week = self.cleaned_data['lesson_day_of_week']
            instance.lesson_type = self.cleaned_data['lesson_type']
            instance.number_of_lessons = self.cleaned_data['number_of_lessons']
            instance.lesson_time = self.cleaned_data['lesson_time']
           
            
            if instance.lesson_start_date > instance.lesson_end_date :
                raise ValidationError ( "The lesson end date must occur after the start date")
            
            if commit:
                instance.save()
                self.save_m2m()
            return instance



class TermForm(forms.ModelForm):
    
    class Meta:
        model = Term
        fields = {"start_of_term_date", 'end_of_term_date', "name" }
        forms.field_order = {"name","start_of_term_date", 'end_of_term_date'}
        widgets = {
            'start_of_term_date' : forms.SelectDateWidget(attrs={'class' : 'form-control'}),
            'end_of_term_date' : forms.SelectDateWidget(attrs={'class' : 'form-control'}),
        }
    def clean(self, *args, **kwargs):
        
        if self.instance.created_at  :
            pass
        else:
            #Do not allow terms with identical names 
            testname = self.cleaned_data['name']
            if Term.objects.filter(name=testname).count() > 0 : 
                raise forms.ValidationError("A term with this name already exists, please choose a different name")

            start_of_term_date = self.cleaned_data['start_of_term_date']
            end_of_term_date= self.cleaned_data['end_of_term_date']

            #Check that the start state occurs before end date
            if start_of_term_date>=end_of_term_date:
                raise forms.ValidationError("The end date can not occur before the start date")

                
            overlap_start_count = Term.objects.filter(start_of_term_date__gte = start_of_term_date , start_of_term_date__lte=end_of_term_date).count()
            overlap_end_count =  Term.objects.filter(end_of_term_date__gte = start_of_term_date, end_of_term_date__lte=end_of_term_date).count()
            overlap_count = overlap_start_count > 0 or overlap_end_count> 0
            if overlap_count > 0 : 
                raise forms.ValidationError("Please select a term date range that does not overlap with the existing terms")
                
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
 

   