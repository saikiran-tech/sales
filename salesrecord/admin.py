from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Salesrecord
# Register your models here.


@admin.register(Salesrecord)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
