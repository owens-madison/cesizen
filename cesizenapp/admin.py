from django.contrib import admin
from .models import Information, StressEvent, Results


# Register your models here.
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('idInformation', 'title', 'content', 'caption', 'category', 'image', 'alt', 'publicationDate')
    readonly_fields = ('idInformation', 'publicationDate')

@admin.register(StressEvent)
class StressEventAdmin(admin.ModelAdmin):
    list_display = ('description', 'score')

@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('min_score', 'max_score', 'description')