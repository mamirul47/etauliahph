from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import TP


class AdminTP(ImportExportModelAdmin):
    list_display = ["cawangan","kelas", "nama", "noKP","status"]
    search_fields = ['nama','noKP','cawangan','kelas','status']

# Register your models here.
admin.site.register(TP,AdminTP)