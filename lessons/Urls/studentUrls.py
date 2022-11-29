from django.urls import path
from ..views import student

urlpatterns =[

    path('home/',student.studentHomePage,name='studentHome'),
    path('request/',student.studentMakeRequest, name = 'request'),
    path('editrequest/<int:my_id>/',student.studentEditRequest, name = 'editrequest'),
    path('editrequest/update/<int:my_id>', student.Editrecord, name='editrecord'),

    
    
]