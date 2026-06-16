from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageview ),
    path('about/', views.aboutusview),
    path('contact/', views.contactusview),
]
