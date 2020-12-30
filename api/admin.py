from django.contrib import admin
from api import models

@admin.register(models.Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    ordering = ['word']
    search_fields = ['word']

@admin.register(models.Guess)
class GuessAdmin(admin.ModelAdmin):
    autocomplete_fields = ['dictionary']

@admin.register(models.Trophy)
class TrophyAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Config)
class ConfigAdmin(admin.ModelAdmin):
    pass
