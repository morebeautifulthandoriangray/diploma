from django.contrib import admin
from .models import Document, Sample, DocumentConsent, DocumentNotification

# Register your models here.

admin.site.register(Document)
admin.site.register(Sample)
admin.site.register(DocumentConsent)
admin.site.register(DocumentNotification)