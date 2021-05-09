from django.urls import path
from . import views

urlpatterns = [
    path('self/', views.self),
    path('qqq/', views.qqq),
    path('', views.index),
]