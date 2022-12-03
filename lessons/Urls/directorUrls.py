from django.urls import path
from ..views import directorViews


urlpatterns =[

    path('home/',directorViews.directorHomePage,name='directorHome'),
    

]