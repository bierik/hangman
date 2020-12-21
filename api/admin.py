from django.contrib import admin
from api import models

@admin.register(models.Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Guess)
class GuessAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Trophy)
class TrophyAdmin(admin.ModelAdmin):
    pass
