from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('landing/', views.landing, name="landing"),
    path('profile/<str:pk>', views.profile, name="profile"),

]