from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageview ),
    path('login/', views.loginpageview),
    path('logout/', views.logoutview),
    path('about/', views.aboutusview),
    path('contact/', views.contactusview),
    path('form/', views.formview),
    path('store/', views.storeview),
    path('add-student/', views.addstudentform),
    path('add-student-process/', views.addstudentformprocess),
    path('students/', views.student_list),
    path('students/add/', views.student_create),
    path('students/edit/<int:student_id>/', views.student_update),
    path('students/delete/<int:student_id>/', views.student_delete),
    path('savesessiondata/', views.savesessiondata),
    path('getsessiondata/', views.getsessiondata),
    path('deletesessiondata/', views.deletesessiondata),
    path('getsessiondata2/', views.getsessiondata2),
    
]
