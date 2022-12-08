from django.urls import path
from ..views import loginViews

urlpatterns =[

   path('signup/',loginViews.signUpPage,name='signUp'),
   path('login/',loginViews.loginPage,name='login'),
   path('logout/',loginViews.logoutPage,name='logout'),

    
]