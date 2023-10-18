from django.urls import path
from . import views
from mainpage.views import *
# from django.conf.urls import url


urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.log, name='login'),
    path('anywhere/', views.anywhere, name='anywhere'),
    path('anywhere/<int:pk>/', views.details, name='details'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('media-example/', views.media_example,name='media'),
    path('add/', views.add, name='add'),
    path('change/<int:pk>/', views.change, name='change'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    # path('profile/', views.profile, name='profile'),
]