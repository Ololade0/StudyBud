from django.urls import path
from . import views
from .views import home, room

app_name = "base"

urlpatterns = [
    path('rooms', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
]