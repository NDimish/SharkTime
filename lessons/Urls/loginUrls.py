from django.urls import path
from ..views import loginViews

urlpatterns =[

   path('register/',loginViews.register_user ,name='registerUser'),
   path('login/' ,loginViews.login_user , name = 'loginUser')

    
]