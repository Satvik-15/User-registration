from django.urls import path
from first_app import views

urlpatterns = [
    path("", views.base),
    path("index/", views.index),
    path("yoyo/", views.yoyo),
    path("login/", views.user_login),
]
