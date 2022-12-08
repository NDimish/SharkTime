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



    path('home/UserShowPage/<int:Logged_ID>/',directorViews.UserShowPage,name='UserShowPage'),
    path('home/StudentShowPage/<int:Logged_ID>/',directorViews.StudentShowPage,name='StudentShowPage'),
    path('home/DirectorShowPage/<int:Logged_ID>/',directorViews.DirectorShowPage,name='DirectorShowPage'),
    path('home/TeacherShowPage/<int:Logged_ID>/',directorViews.TeacherShowPage,name='TeacherShowPage'),
    path('home/PaymentShowPage/<int:Logged_ID>/',directorViews.PaymentShowPage,name='PaymentShowPage'),
    path('home/Sys_userShowPage/<int:Logged_ID>/',directorViews.Sys_userShowPage,name='Sys_userShowPage'),
    path('home/Sys_authorityShowPage/<int:Logged_ID>/',directorViews.Sys_authorityShowPage,name='Sys_authorityShowPage'),
    path('home/Sys_user_authorityShowPage/<int:Logged_ID>/',directorViews.Sys_user_authorityShowPage,name='Sys_user_authorityShowPage'),
    path('home/LessonShowPage/<int:Logged_ID>/',directorViews.LessonShowPage,name='LessonShowPage'),
    path('home/LessonRequestShowPage/<int:Logged_ID>/',directorViews.LessonRequestShowPage,name='LessonRequestShowPage'),
    path('home/LessonBookingShowPage/<int:Logged_ID>/',directorViews.LessonBookingShowPage,name='LessonBookingShowPage'),


    

]