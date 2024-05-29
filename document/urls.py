from django.urls import path, include
from django.contrib import admin
# DocumentListView
from .views import ( DocumentConsentListView,
                     DocumentConsentCreateView,
                     SampleListView, SampleCreateView,
                     SampleDetailView, SampleUpdateView,
                     SampleDeleteView, DocumentConsentDetailView,
                     DocumentConsentUpdateView, DocumentConsentDeleteView,
                     FileDownloadDocx, FileDownloadPdf, DocumentConsentDownloadDocx, DocumentConsentDownloadPDF,


                     DocumentNotificationListView,
                     DocumentNotificationDetailView,
                     DocumentNotificationUpdateView,
                     DocumentNotificationDeleteView,
                     DocumentNotificationCreateView,
                     DocumentNotificationDownloadDocx,


                     DocumentAuthorsAwardListView,
                     DocumentAuthorsAwardDetailView,
                     DocumentAuthorsAwardUpdateView,
                     DocumentAuthorsAwardDeleteView,
                     DocumentAuthorsAwardCreateView,
                     DocumentAuthorsAwardDownloadDocx)
from django.views.generic import TemplateView
from document import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('documents/', TemplateView.as_view(template_name='documents_all.html'), name='documents_all'),
#     document consent
    path('documents/consent/', DocumentConsentListView.as_view(), name='documents_consent_all'),
    path('documents/consent/new/', DocumentConsentCreateView.as_view(), name='document_consent_new'),
    path('documents/consent/<int:pk>/', DocumentConsentDetailView.as_view(), name='document_consent_detail'),
    path('documents/consent/<int:pk>/edit', DocumentConsentUpdateView.as_view(), name='document_consent_edit'),
    path('documents/consent/<int:pk>/delete', DocumentConsentDeleteView.as_view(), name='document_consent_delete'),
    path('documents/consent/<int:pk>/download_docx/', DocumentConsentDownloadDocx.as_view(), name='document_consent_download_docx'),
    path('documents/consent/<int:pk>/download_pdf/', DocumentConsentDownloadPDF.as_view(),
         name='document_consent_download_pdf'),

    #     sample document
    path('samples/', SampleListView.as_view(), name='samples_all'),
    path('samples/<int:pk>/', SampleDetailView.as_view(), name='sample_detail'),
    path('samples/new/', SampleCreateView.as_view(), name='sample_new'),
    path('samples/<int:pk>/edit/', SampleUpdateView.as_view(), name='sample_edit'),
    path('samples/<int:pk>/delete/', SampleDeleteView.as_view(), name='sample_delete'),
    path('samples/<int:pk>/download_docx/', FileDownloadDocx.as_view() , name='sample_download_docx'),
    path('samples/<int:pk>/download_pdf/', FileDownloadPdf.as_view(), name='sample_download_pdf'),

#     document notification
    path('documents/notification/', DocumentNotificationListView.as_view(), name='documents_notification_all'),
    path('documents/notification/new/', DocumentNotificationCreateView.as_view(), name='document_notification_new'),
    path('documents/notification/<int:pk>/', DocumentNotificationDetailView.as_view(), name='document_notification_detail'),
    path('documents/notification/<int:pk>/edit', DocumentNotificationUpdateView.as_view(), name='document_notification_edit'),
    path('documents/notification/<int:pk>/delete', DocumentNotificationDeleteView.as_view(), name='document_notification_delete'),
    path('documents/notification/<int:pk>/download_docx/', DocumentNotificationDownloadDocx.as_view(),
         name='document_notification_download_docx'),

#
    path('documents/authors_award/', DocumentAuthorsAwardListView.as_view(), name='documents_authors_award_all'),
    path('documents/authors_award/new/', DocumentAuthorsAwardCreateView.as_view(), name='document_authors_award_new'),
    path('documents/authors_award/<int:pk>/', DocumentAuthorsAwardDetailView.as_view(), name='document_authors_award_detail'),
    path('documents/authors_award/<int:pk>/edit', DocumentAuthorsAwardUpdateView.as_view(), name='document_authors_award_edit'),
    path('documents/authors_award/<int:pk>/delete', DocumentAuthorsAwardDeleteView.as_view(), name='document_authors_award_delete'),
    path('documents/authors_award/<int:pk>/download_docx/', DocumentAuthorsAwardDownloadDocx.as_view(),
         name='document_authors_award_download_docx'),


]