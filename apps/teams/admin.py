from django.contrib import admin
from . import models

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'token'),
        'is_active',
        ('is_staff', 'is_superuser'),
        'last_login',
#        'password',
    )

    search_fields = ('name', )
    readonly_fields = ('last_login', 'password')

admin.site.register(models.Team, TeamAdmin)