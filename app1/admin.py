from django.contrib import admin
from app1.models import Ques
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Ques)
class Q(ImportExportModelAdmin):
	pass