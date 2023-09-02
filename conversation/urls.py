
from django.urls import path
from . import views

urlpatterns = [
   
    path('new/<int:pk>', views.new_Conversation,name='new_conversation'),
    path('inbox/', views.inbox,name='inbox'),
    path('messages/<int:pk>', views.conversationDetail,name='messages'),
    
    
   
 
]
