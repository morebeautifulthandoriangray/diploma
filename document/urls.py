from django.urls import path, include
from django.contrib import admin
# DocumentListView
from .views import  DocumentConsentListView, DocumentConsentCreateView, SampleListView, SampleCreateView, SampleDetailView, SampleUpdateView, SampleDeleteView, DocumentConsentDetailView
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('documents/', TemplateView.as_view(template_name='documents_all.html'), name='documents_all'),
    path('documents/consent/', DocumentConsentListView.as_view(), name='documents_consent_all'),
    path('documents/new/', DocumentConsentCreateView.as_view(), name='document_new'),
    path('documents/<int:pk>/', DocumentConsentDetailView.as_view(), name='document_detail'),
    path('samples/', SampleListView.as_view(), name='samples_all'),
    path('samples/<int:pk>/', SampleDetailView.as_view(), name='sample_detail'),
    path('samples/new/', SampleCreateView.as_view(), name='sample_new'),
    path('samples/<int:pk>/edit/', SampleUpdateView.as_view(), name='sample_edit'),
    path('samples/<int:pk>/delete/', SampleDeleteView.as_view(), name='sample_delete'),
]