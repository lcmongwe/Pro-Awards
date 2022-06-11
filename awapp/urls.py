from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns =[
    path('', views.home, name="home"),
    path('landing/', views.landing, name="landing"),
    path('create_profile/<user_id>', views.create_profile, name="create_profile"),   
    path('profile/<str:pk>', views.profile, name="profile"),
    path('post',views.create_post,name='post'),
    path('update_post/<str:pk>', views.update_post, name='update_post'),
    path('delete_post/<str:pk>', views.delete_post, name='delete_post'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)