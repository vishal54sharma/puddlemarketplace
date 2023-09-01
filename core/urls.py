
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('signup/', views.signupUser,name='signupUser'),
    path('login/', views.loginUser,name='loginUser'),
    path('logout/', views.logoutUser,name='logoutUser'),
    path('about/', views.aboutUs,name='aboutUs'),
    
 
]
