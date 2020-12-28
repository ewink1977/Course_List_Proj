from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add_course', views.add_course, name = 'add_course'),
]
