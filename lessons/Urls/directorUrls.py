from django.urls import path
from ..views import directorViews


urlpatterns =[

    path('home/<int:Logged_ID>',directorViews.directorHomePage,name='directorHome'),
    

]