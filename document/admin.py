from django.contrib import admin
from .models import Document, Sample, DocumentConsent, DocumentNotification, DocumentAuthorsAward, DocumentSet, \
    ReviewProblemSample, ReviewProblemDocumentConsent, HeadOfficer, Status, SignDocument



class HeadOfficerAdmin(admin.ModelAdmin):
    list_display = ('id', 'FIO_head')
    list_display_links = ('id', 'FIO_head')
    search_fields = ('FIO_head', )

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status',)
    list_display_links = ('id', 'status')
    search_fields = ('status', )

class SignDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_consent_name', 'status', 'FIO_head')
    list_display_links = ('id', 'document_consent_name')
    search_fields = ('document_consent_name', 'FIO_head', 'status')


class SampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'path_to_template')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'created_at', 'path_to_template')


class DocumentConsentAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'title', 'created_at', 'template_name', 'path_to_template', 'program_name', 'applicant_surname',
    'applicant_name')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'created_at', 'program_name', 'applicant_surname', 'applicant_name')


class DocumentNotificationAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'title', 'created_at', 'template_name', 'program_name', 'applicant1_surname', 'applicant2_surname',
    'current_date')
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


class DocumentSetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'template_name', 'document_consent', 'document_notification', 'document_authors_award')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'template_name', 'document_consent', 'document_notification', 'document_authors_award')


# Добавить еще документы для кастомизированного отображения документов.

class ReviewProblemSampleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'review_problem_sample_title', 'sample_name', 'user_id', 'user_name', 'review_text')

    list_display_links = ('id', 'review_problem_sample_title')
    search_fields = ('review_problem_sample_title', 'sample_name')


# Добавить еще документы для кастомизированного отображения документов.

class ReviewProblemDocumentConsentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'review_problem_document_consent_title', 'document_consent_name', 'user_id', 'user_name', 'review_text')
    list_display_links = ('id', 'review_problem_document_consent_title')
    search_fields = ('title', 'review_problem_document_consent_title', 'document_consent_name')


# Добавить еще документы для кастомизированного отображения документов.


# admin.site.register(Document)
admin.site.register(Sample, SampleAdmin)
admin.site.register(DocumentConsent, DocumentConsentAdmin)
admin.site.register(DocumentNotification, DocumentNotificationAdmin)
admin.site.register(DocumentAuthorsAward, DocumentAuthorsAwardAdmin)
admin.site.register(DocumentSet, DocumentSetAdmin)
admin.site.register(ReviewProblemSample, ReviewProblemSampleAdmin)
admin.site.register(ReviewProblemDocumentConsent, ReviewProblemDocumentConsentAdmin)


admin.site.register(HeadOfficer, HeadOfficerAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(SignDocument, SignDocumentAdmin)

admin.site.site_title = "Панель управление приложением"
admin.site.site_header = "Панель управление приложением"
