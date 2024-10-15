from django.urls import path
from . import views

app_name = 'dataimport'  # Set this to the name of your app

urlpatterns = [
    path('home/', views.home, name='home'),
    path('province-table/', views.province_table, name='province-table'),
    path('data-import-province-table-ajax', views.data_import_province_table_ajax,
         name="data_import_province_table_ajax"),
    path('data-import-province-from-github', views.data_import_province_from_github,
         name="data_import_province_from_github"),
]
