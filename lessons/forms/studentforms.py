from django import forms
from ..models.requests import request
from ..models import requests




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
        instance.lesson_teacher=self.cleaned_data['lesson_teacher']
        instance.student_id = self.cleaned_data['student_id']
        instance.lesson_start_date = self.cleaned_data['lesson_start_date']
        instance.lesson_duration = self.cleaned_data['lesson_duration']
        instance.lesson_interval = self.cleaned_data['lesson_interval']
        instance.lesson_type = self.cleaned_data['lesson_type']
        instance.number_of_lessons = self.cleaned_data['number_of_lessons']
        instance.lesson_time = self.cleaned_data['lesson_time']
        if commit:
            instance.save()
         
        return instance






















