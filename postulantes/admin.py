from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Postulante)
#admin.site.register(Documento)

class PostulanteResources(ImportExportModelAdmin, admin.ModelAdmin):

    class Meta:
        model = Postulante

admin.site.register(Postulante, PostulanteResources)


