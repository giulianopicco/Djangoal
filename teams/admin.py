from django.contrib import admin
from teams import models

# Register your models here.


class PlayerInline(admin.TabularInline):
    model = models.Player


class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]


admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.Player)