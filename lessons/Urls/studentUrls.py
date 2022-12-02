from django.urls import path
from ..views import student
from ..views import loginviews

urlpatterns =[

    path('home/',student.studentHomePage),
    path('request/',student.studentMakeRequest, name = 'request'),
    path('student_home/',loginviews.student_home, name = 'student_home'),
    #path('', loginviews.home, name='home'),
    # path('home/', loginviews.sign_up, name='sign_up'),
    # path('home/', loginviews.log_in, name='log_in'),
    path('sign_up/', loginviews.sign_up, name='sign_up'),
    path('log_in/', loginviews.log_in, name='log_in')

]
