from django.urls import path, re_path
from core import views

urlpatterns = [
    path('chatrooms/', views.chatrooms, name="chatrooms"),
    path('chatrooms/<slug:slug>', views.chatroom_detail, name="chatroom_detail"),
    path('chat/', views.app, name='twilio'),
    re_path(r'^token', views.token, name='token'),
]


