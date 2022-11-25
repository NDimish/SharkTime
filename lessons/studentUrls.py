from django.urls import path
from .views import student

urlpatterns =[

    path('home/',student.studentHomePage),
    path('request/',student.studentMakeRequest, name = 'request'),

]