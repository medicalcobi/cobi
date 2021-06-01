from django.urls import path
from . import views

urlpatterns = [
    path('self/', views.self),
    path('qqq/', views.qqq),
    path('searchhospital/', views.searchhospital),
    path('search_hospital_seoul/', views.search_hospital_seoul),
    path('search_hospital_incheon/', views.search_hospital_incheon),
    path('search_hospital_busan/', views.search_hospital_busan),
    path('', views.landing),
]