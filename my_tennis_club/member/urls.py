from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('members_list/', views.members_list, name='members_list'),
]