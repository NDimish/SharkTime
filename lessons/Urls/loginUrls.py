from django.urls import path
from ..views import loginViews

urlpatterns =[

   path('signup/',loginViews.signUpPage,name='signUp'),

    
]