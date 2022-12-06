from django.urls import path
from ..views import student

urlpatterns =[

   path('home/<int:Logged_ID>/',student.studentHomePage,name='studentHome'),
    path('home/<int:Logged_ID>/viewRequests/',student.studentViewRequests,name='studentViewRequests'),
    path('request/<int:Logged_ID>/',student.studentMakeRequest, name = 'request'),
    path('editrequest/<int:Logged_ID>/<int:my_id>/',student.studentEditRequest, name = 'editrequest'),
    path('editrequest/update/<int:Logged_ID>/<int:my_id>', student.Editrecord, name='editrecord'),
    
    
]