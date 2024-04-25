from django.urls import path, include
from django.contrib import admin
# DocumentListView
from .views import DocumentConsentListView, DocumentConsentCreateView, SampleListView, SampleCreateView, SampleDetailView, SampleUpdateView, SampleDeleteView, DocumentConsentDetailView, DocumentConsentUpdateView, DocumentConsentDeleteView
from django.views.generic import TemplateView
# from .views import read_sample_word2thml


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('documents/', TemplateView.as_view(template_name='documents_all.html'), name='documents_all'),
    path('documents/consent/', DocumentConsentListView.as_view(), name='documents_consent_all'),
    path('documents/consent/new/', DocumentConsentCreateView.as_view(), name='document_consent_new'),
    path('documents/consent/<int:pk>/', DocumentConsentDetailView.as_view(), name='document_consent_detail'),
    path('documents/consent/<int:pk>/edit', DocumentConsentUpdateView.as_view(), name='document_consent_edit'),
    path('documents/consent/<int:pk>/delete', DocumentConsentDeleteView.as_view(), name='document_consent_delete'),
    path('samples/', SampleListView.as_view(), name='samples_all'),
    path('samples/<int:pk>/', SampleDetailView.as_view(), name='sample_detail'),
    path('samples/new/', SampleCreateView.as_view(), name='sample_new'),
    path('samples/<int:pk>/edit/', SampleUpdateView.as_view(), name='sample_edit'),
    path('samples/<int:pk>/delete/', SampleDeleteView.as_view(), name='sample_delete'),
    # path('samples/<int:pk>/read_word/', read_sample_word2thml, name='sample_read'),

]