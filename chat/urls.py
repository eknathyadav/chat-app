from django.urls import path
from . import views
app_name = "chat"
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:room_name>/', views.room, name="room"),
    path('user/login/', views.loginUser, name="login"),
    path('user/logout/', views.logoutUser, name="logout"),
    path('user/register/', views.registerUser, name="register"),
    path('user/create-room/', views.createRoom, name="create-room"),
    path('user/join-room/', views.joinRoom, name="join-room"),
]
