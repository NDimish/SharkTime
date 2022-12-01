from django import forms
from ..models.models import LessonBook as request

#student forms

class make_request(forms.ModelForm):

    class Meta:
        model = request
        fields =[

        
        'book_date',
        'booking_time',
        'book_duration',
        'lesson_type'

        
        ]

    def save(self):
        """Create a new user."""

        super().save(commit=False)
        user = request.objects.create(
            lesson_type = "sadas",
            booking_time = self.cleaned_data.get('booking_time'),
            student_id = 1,
            remarks = "usdfisad",
            book_duration =self.cleaned_data.get('book_duration'),
            book_date = self.cleaned_data.get('book_date'),
            book_status = "P"
            
        )
        
        return user

