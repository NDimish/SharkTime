from django import forms
from ..models.requests import request
from ..models import requests
from multiselectfield import MultiSelectFormField
from multiselectfield import MultiSelectField



#student forms
class make_request(forms.ModelForm):
    # availability =  forms.CharField(
    # label='Enter a keyword to search for',
    # widget=forms.TextInput(attrs={'size': 32})
    # )
    # availability = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    
    #                                      choices=requests.DAY_OF_WEEK_CHOICES)
    # availability = forms.ModelMultipleChoiceField(queryset=requests.Weekday.objects.all(),widget=forms.CheckboxSelectMultiple)
    # #availability = forms.ModelMultipleChoiceField(queryset=requests.Weekday.objects, widget=forms.CheckboxSelectMultiple, required=False)

    # def __init__ (self,*args, **kwargs):
    #     if kwargs.get('instance'):
    #         initial = kwargs.setdefault('initial', {})
    #         initial['availability'] = [a.pk for a in kwargs['instance'].availability.all()]
    #     forms.ModelForm.__init__(self,*args, **kwargs)
    
    class Meta:
        model = request
        fields =(
        'lesson_teacher',
        'lesson_start_date',
        #'availability',
        'lesson_duration',
        'lesson_interval',
        'lesson_type',
        'number_of_lessons',
        'student_id',
        'lesson_time'
        )
    #labels = {'availability' : "Days You Are Available For Lessons"}  
    #widgets = {'availability'  : forms.CheckboxSelectMultiple(attrs={'class' : 'form-control'}) }
    
     
    

    def save(self, commit=True):
        """Create a new user."""
        instance = forms.ModelForm.save(self,False)

        # old_save_m2m = self.save_m2m
        # def save_m2m():
        #     old_save_m2m()
        #     instance.availability.clear()
        #     instance.availability.add(*self.cleaned_data['availability'])
        # self.save_m2m = save_m2m
     
        # self.cleaned_data.get('username'),
        instance.lesson_teacher=self.cleaned_data['lesson_teacher']
        instance.student_id = self.cleaned_data['student_id']
        #instance.student_id = 1
        instance.lesson_start_date = self.cleaned_data['lesson_start_date']
        instance.lesson_duration = self.cleaned_data['lesson_duration']
        instance.lesson_interval = self.cleaned_data['lesson_interval']
        instance.lesson_type = self.cleaned_data['lesson_type']
        instance.number_of_lessons = self.cleaned_data['number_of_lessons']
        instance.lesson_time = self.cleaned_data['lesson_time']
         
         
        if commit:
            instance.save()
            self.save_m2m()
        # super().save(commit=False)
        # user = request.objects.create(
        #    # self.cleaned_data.get('username'),
        #     lesson_teacher=self.cleaned_data.get('lesson_teacher'),
        #     student_id=self.cleaned_data.get('student_id'),
        #     Date=self.cleaned_data.get('Date'),
        #     lesson_duration=self.cleaned_data.get('lesson_duration'),
        #     lesson_interval=self.cleaned_data.get('lesson_interval'),
        #     lesson_type=self.cleaned_data.get('lesson_type'),
        #     number_of_lessons=self.cleaned_data.get('number_of_lessons'),
        #     availability = self.cleaned_data.get('availability') 
        #     # = self.cleaned_data.get('availability')
        # )

        
        
       # super().save(commit=False)
        return instance

#PREVIOUS VERSION make_request

# class make_request(forms.ModelForm):

#     class Meta:
#         model = request
#         fields =[

        
#        'Teacher',
#         'Date',
#         'time',
#         'durations',
#         'lesson_type'

        
#         ]

    # def save(self):
        
    #     #-------Create a new user.

    #     super().save(commit=False)
    #     user = request.objects.create(
    #        # self.cleaned_data.get('username'),
    #         Teacher=self.cleaned_data.get('Teacher'),
    #         Student = 'testbob',
    #         Date=self.cleaned_data.get('Date'),
    #         time=self.cleaned_data.get('time'),
    #         durations=self.cleaned_data.get('durations'),
    #         lesson_type=self.cleaned_data.get('lesson_type'),
    #     )
    #     return user





















