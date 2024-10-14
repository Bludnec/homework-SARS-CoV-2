from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('province-table/', views.province_table, name='province-table'),
]
