from django.contrib import admin

from . import models


@admin.register(models.Drawing)
class DrawingsAdmin(admin.ModelAdmin):
    pass
