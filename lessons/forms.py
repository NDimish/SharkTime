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

    def save(self):
        """Create a new user."""

        super().save(commit=False)
        user = request.objects.create(
           # self.cleaned_data.get('username'),
            Teacher=self.cleaned_data.get('Teacher'),
            Student = 'wewe',
            Date=self.cleaned_data.get('Date'),
            time=self.cleaned_data.get('time'),
            durations=self.cleaned_data.get('durations'),
            lesson_type=self.cleaned_data.get('lesson_type'),
        )
        return user

