from django.contrib import admin
from testapp.models import Food_Requested, Organization

# Register your models here.

admin.site.register(Food_Requested)
admin.site.register(Organization)