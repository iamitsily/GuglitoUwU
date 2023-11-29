from django.urls import path
from ilysdjangoApp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("yahir/", views.yahir),
    
]