from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.userindex, name='userindex'),
    path('user/',views.index, name='index')
]