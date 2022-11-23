from django.urls import path
from .views import student

urlpatterns =[

    path('home/',student.studentHomePage),
    path('button/',student.button,name="button")
]