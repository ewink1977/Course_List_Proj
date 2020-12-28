from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add_course', views.add_course, name = 'add_course'),
    path('destroy/<killid>', views.destroy_course, name='destroy_course'),
]
