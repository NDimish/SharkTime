from django.urls import path
from ..views import adminViews

urlpatterns =[

    path('home/',adminViews.admin_home),
    path('<int:id>', adminViews.view_request, name='view_request')

]