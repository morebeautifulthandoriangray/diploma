from django.contrib import admin
from .models import Document, Sample, DocumentConsent, DocumentNotification, DocumentAuthorsAward

# Register your models here.

class SampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'path_to_template')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'created_at', 'path_to_template')
    # fields =

    # def get_file(self, obj):
    #     return mark_safe(f'')


# Добавить еще документы для кастомизированного отображения документов.


admin.site.register(Document)
admin.site.register(Sample, SampleAdmin)
admin.site.register(DocumentConsent)
admin.site.register(DocumentNotification)
admin.site.register(DocumentAuthorsAward)

admin.site.site_title = "Панель управление приложением"
admin.site.site_header = "Панель управление приложением"