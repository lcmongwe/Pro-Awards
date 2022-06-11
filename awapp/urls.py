from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns =[
    path('', views.home, name="home"),
    path('landing/', views.landing, name="landing"),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('post',views.create_post,name='post'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)