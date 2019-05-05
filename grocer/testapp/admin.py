from django.contrib import admin
from testapp import models

# Register your models here.

admin.site.register(models.Food_Requested)
admin.site.register(models.Food_Produced)
admin.site.register(models.Producer)
admin.site.register(models.Requester)
admin.site.register(models.Cater)
