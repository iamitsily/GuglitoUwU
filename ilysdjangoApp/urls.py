from django.urls import path
from ilysdjangoApp import views
from ilysdjangoApp import templates

urlpatterns = [
    path("", views.home, name="home"),
    path("yahir/", templates.yahir, name="yahir"),
    
]