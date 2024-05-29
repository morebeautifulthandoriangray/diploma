from django.contrib import admin
from .models import Document, Sample, DocumentConsent, DocumentNotification, DocumentAuthorsAward


# Register your models here.

class SampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'path_to_template')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'created_at', 'path_to_template')


class DocumentConsentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'template_name', 'program_name', 'applicant_surname', 'applicant_name')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'created_at', 'program_name', 'applicant_surname', 'applicant_name')


class DocumentNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'template_name', 'program_name', 'applicant1_surname', 'applicant2_surname', 'current_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'created_at', 'program_name', 'applicant1_surname', 'applicant2_surname', 'current_date')


class DocumentAuthorsAwardAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'title', 'template_name', 'program_name', 'applicant1_surname', 'applicant2_surname',
    'authors_award')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'program_name', 'applicant1_surname', 'applicant2_surname', 'authors_award')

    # def get_file(self, obj):
    #     return mark_safe(f'')


# Добавить еще документы для кастомизированного отображения документов.


# admin.site.register(Document)
admin.site.register(Sample, SampleAdmin)
admin.site.register(DocumentConsent, DocumentConsentAdmin)
admin.site.register(DocumentNotification, DocumentNotificationAdmin)
admin.site.register(DocumentAuthorsAward, DocumentAuthorsAwardAdmin)

admin.site.site_title = "Панель управление приложением"
admin.site.site_header = "Панель управление приложением"
