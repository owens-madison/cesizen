from django.contrib import admin
from .models import Information, Diagnostic, StressEvent


# Register your models here.
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('idInformation', 'title', 'content', 'caption', 'category', 'image', 'alt', 'publicationDate')
    readonly_fields = ('idInformation', 'publicationDate')

@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('score', 'result', 'diagnosticDate', 'diagnosticUser')
    readonly_fields = ('score', 'result', 'diagnosticDate', 'diagnosticUser')

@admin.register(StressEvent)
class StressEventAdmin(admin.ModelAdmin):
    list_display = ('description', 'score')