
from django.urls import path
from . import views

urlpatterns = [
    path('', views.searchItem,name='searchItem'),
    path('new/', views.new,name='new'),
    path('<int:pk>', views.detail,name='detail'),
    path('delete/<int:pk>', views.deleteItem , name='deleteItem' ),
    path('edit/<int:pk>', views.editItem , name='editItem' ),
    
   
 
]
