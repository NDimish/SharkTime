from django.urls import path
from ..views import directorViews


urlpatterns =[

    path('home/<int:Logged_ID>',directorViews.directorHomePage,name='directorHome'),
    path('home/UserFormPage/<int:Logged_ID>/<int:my_id>',directorViews.UserFormPage,name='UserFormPage'),
    path('home/StudentFormPage/<int:Logged_ID>/<int:my_id>',directorViews.StudentFormPage,name='StudentFormPage'),
    path('home/DirectorFormPage/<int:Logged_ID>/<int:my_id>',directorViews.DirectorFormPage,name='DirectorFormPage'),
    path('home/TeacherFormPage/<int:Logged_ID>/<int:my_id>',directorViews.TeacherFormPage,name='TeacherFormPage'),
    path('home/PaymentFormPage/<int:Logged_ID>/<int:my_id>',directorViews.PaymentFormPage,name='PaymentFormPage'),
    path('home/Sys_userFormPage/<int:Logged_ID>/<int:my_id>',directorViews.Sys_userFormPage,name='Sys_userFormPage'),
    path('home/Sys_authorityFormPage/<int:Logged_ID>/<int:my_id>',directorViews.Sys_authorityFormPage,name='Sys_authorityFormPage'),
    path('home/Sys_user_authorityFormPage/<int:Logged_ID>/<int:my_id>',directorViews.Sys_user_authorityFormPage,name='Sys_user_authorityFormPage'),
    path('home/LessonFormPage/<int:Logged_ID>/<int:my_id>',directorViews.LessonFormPage,name='LessonFormPage'),
    path('home/LessonRequestFormPage/<int:Logged_ID>/<int:my_id>',directorViews.LessonRequestFormPage,name='LessonRequestFormPage'),
    path('home/LessonBookingFormPage/<int:Logged_ID>/<int:my_id>',directorViews.LessonBookingFormPage,name='LessonBookingFormPage'),


    

]