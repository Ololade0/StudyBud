from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('topics/', views.topicsPage, name="topics"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

]
