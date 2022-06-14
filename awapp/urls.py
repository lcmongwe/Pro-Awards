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
    path('review/<post_id>', views.review, name="review"),
    path('search', views.search, name="search"),

  # api-views

    path('posts/', views.post_list, name="posts"),
    path('posts/<int:id>', views.post_detail, name="posts"),
    path('profiles/', views.profile_list, name="profiles"),
    path('profiles/<int:id>', views.profile_detail, name="profiles"),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)