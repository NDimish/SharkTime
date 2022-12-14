from django import forms
from lessons.models import LessonRequest as request

#student forms
class make_request(forms.ModelForm):
    class Meta:
        model = request
        fields =(
        'lesson_teacher',
        'lesson_start_date',
        'lesson_duration',
        'lesson_interval',
        'lesson_day_of_week',
        'lesson_type',
        'number_of_lessons',
        'student_id',
        'lesson_time'
        )

    def save(self, commit=True):
        """Create a new user."""
        instance = forms.ModelForm.save(self,False)
        instance.lesson_teacher=self.cleaned_data['lesson_teacher']
        instance.student_id = self.cleaned_data['student_id']
        instance.lesson_start_date = self.cleaned_data['lesson_start_date']
        instance.lesson_duration = self.cleaned_data['lesson_duration']
        instance.lesson_interval = self.cleaned_data['lesson_interval']
        instance.lesson_day_of_week = self.cleaned_data['lesson_day_of_week']
        instance.lesson_type = self.cleaned_data['lesson_type']
        instance.number_of_lessons = self.cleaned_data['number_of_lessons']
        instance.lesson_time = self.cleaned_data['lesson_time']
        instance.submit_depend_id = self.cleaned_data['student_id']
        if commit:
            instance.save()

        return instance
