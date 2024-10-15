from django.contrib import admin

from dataimport.models import DataImportProvince, DataImportConfiguration

# Register your models here.
admin.site.register(DataImportProvince)
admin.site.register(DataImportConfiguration)
