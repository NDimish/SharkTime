from django.urls import path
from ..views import adminViews

urlpatterns =[

    path('home/',adminViews.admin_home, name='adminHome'),
    path('viewStudents/',adminViews.view_students, name='adminViewStudents'),
    path('viewRequests/',adminViews.view_requests, name='adminViewRequests'),
    path('viewTransactions/',adminViews.view_transactions, name='adminViewTransactions'),
    path('viewTermDates/',adminViews.view_term_dates, name='adminViewTermDates'),
    path('addTermDates/',adminViews.add_term, name='add_term'), 
    path('editTermDates/<int:id>/',adminViews.update_term, name='update_term'), 
    path('editTermDates/update/<int:id>/',adminViews.edit_a_term, name='edit_a_term'), 
    path('<int:id>', adminViews.view_request, name='view_request'),
    path('addBooking/<int:id>/', adminViews.add_booking, name = 'add_booking'),
    path('editBooking/<int:id>/', adminViews.edit_booking, name = 'edit_booking'),
    path('editBooking/update/<int:id>', adminViews.editBookingRecord, name='editBookingRecord'),
    

]