from django import forms
from lessons import models

#director forms
class Userform(forms.ModelForm):
    class Meta:
        model = models.User
        fields ='__all__'
    def save(self, commit=True):
        return

class Studentform(forms.ModelForm):
    class Meta:
        model = models.Student
        fields ='__all__'

    def save(self, commit=True):
        return

class Directorform(forms.ModelForm):
    class Meta:
        model = models.Director
        fields ='__all__'

    def save(self, commit=True):
        return

class Teacherform(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields ='__all__'

    def save(self, commit=True):
        return


class Paymentform(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields ='__all__'

    def save(self, commit=True):
        return

class Sys_user_form(forms.ModelForm):
    class Meta:
        model = models.Sys_user
        fields ='__all__'

    def save(self, commit=True):
        return

class Sys_authority_form(forms.ModelForm):
    class Meta:
        model = models.Sys_authority
        fields ='__all__'

    def save(self, commit=True):
        return

class Sys_user_authority_form(forms.ModelForm):
    class Meta:
        model = models.Sys_user_authority
        fields ='__all__'

    def save(self, commit=True):
        return

class Lessonsform(forms.ModelForm):
    class Meta:
        model = models.Lesson
        fields ='__all__'

    def save(self, commit=True):
        return

class LessonRequestform(forms.ModelForm):
    class Meta:
        model = models.LessonRequest
        fields ='__all__'

    def save(self, commit=True):
        return


class LessonBookingform(forms.ModelForm):
    class Meta:
        model = models.LessonBooking
        fields ='__all__'

    def save(self, commit=True):
        return
