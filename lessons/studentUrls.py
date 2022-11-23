from django.urls import path
from . import student

urlpatterns =[

    path('home/',student.userDetails),
    path('button/',student.button,name="button")
]