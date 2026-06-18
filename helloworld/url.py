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
    path('savesessiondata/', views.savesessiondata),
    path('getsessiondata/', views.getsessiondata),
    path('deletesessiondata/', views.deletesessiondata),
    path('getsessiondata2/', views.getsessiondata2),
    
]
