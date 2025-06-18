from django.contrib import admin
from .models import Information, Comment, Diagnostic

# Register your models here.
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('idInformation', 'title', 'content', 'caption', 'category', 'image', 'alt', 'publicationDate')
    readonly_fields = ('idInformation', 'publicationDate')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('idComment', 'comment', 'commenter', 'commentDate')
    readonly_fields = ('idComment', 'commenter', 'commentDate')

@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('score', 'result', 'diagnosticDate', 'diagnosticUser')
    readonly_fields = ('score', 'result', 'diagnosticDate', 'diagnosticUser')