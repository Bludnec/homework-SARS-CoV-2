from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='about'),
    path('province-table/', views.province_table, name='about'),
]
