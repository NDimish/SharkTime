from django.urls import path
from ..views import adminViews

urlpatterns =[

    path('home/',adminViews.admin_home, name='adminHome'),
    path('<int:id>', adminViews.view_request, name='view_request'),
    path('addBooking/<int:id>/', adminViews.add_booking, name = 'add_booking'),
    

]