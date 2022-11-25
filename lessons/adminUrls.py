from django.urls import path
from .views import adminViews

urlpatterns =[

    path('home/',adminViews.admin_home),


]