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
                     DocumentAuthorsAwardDownloadDocx,


                     DocumentSetListView,
                     DocumentSetsCreateView,
                    DocumentSetsDetailView,
                    DocumentSetsUpdateView,
                    DocumentSetsDeleteView,
                    DocumentSetsDownloadDocx,
                    DocumentSetsDownloadPDF,

ReviewProblemSampleCreateView,
ReviewProblemDocumentConsentCreateView,

SignDocumentCreateView,
SignDocumentDetailView,
SignDocumentListView,
SignDocumentDeleteView,
# SignDocumentUpdateView,
HeadSignDocumentCreateView,
HeadSignDocumentListView,
HeadSignDocumentDetailView,
HeadSignDocumentDetailView,
HeadSignDocumentDeleteView,
HeadSignDocumentUpdateView
                     )
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

# document authors award
    path('documents/authors_award/', DocumentAuthorsAwardListView.as_view(), name='documents_authors_award_all'),
    path('documents/authors_award/new/', DocumentAuthorsAwardCreateView.as_view(), name='document_authors_award_new'),
    path('documents/authors_award/<int:pk>/', DocumentAuthorsAwardDetailView.as_view(), name='document_authors_award_detail'),
    path('documents/authors_award/<int:pk>/edit', DocumentAuthorsAwardUpdateView.as_view(), name='document_authors_award_edit'),
    path('documents/authors_award/<int:pk>/delete', DocumentAuthorsAwardDeleteView.as_view(), name='document_authors_award_delete'),
    path('documents/authors_award/<int:pk>/download_docx/', DocumentAuthorsAwardDownloadDocx.as_view(),
         name='document_authors_award_download_docx'),


# document  package all
    path('documents/sets/', TemplateView.as_view(template_name='document_doc_pack/documents_sets_all.html'), name='documents_sets_all'),

    path('documents/sets/patent/', DocumentSetListView.as_view(), name='document_sets_all_detail'),
    path('documents/sets/patent/new', DocumentSetsCreateView.as_view(), name='document_sets_new'),
    path('documents/sets/patent/<int:pk>/', DocumentSetsDetailView.as_view(), name='document_set_detail'),
    path('documents/sets/patent/<int:pk>/edit', DocumentSetsUpdateView.as_view(), name='document_sets_edit'),
    path('documents/sets/patent/<int:pk>/delete', DocumentSetsDeleteView.as_view(), name='document_sets_delete'),
    path('documents/sets/patent/<int:pk>/download_docx/', DocumentSetsDownloadDocx.as_view(),name='document_sets_download_docx'),
    path('documents/sets/patent/<int:pk>/download_pdf/', DocumentSetsDownloadPDF.as_view(),
         name='document_sets_download_pdf'),

    # document  review

    path('documents/reviews',
         TemplateView.as_view(template_name='review_problems.html'),
         name='review_problems'),

    # path('documents/reviews/review_sample', TemplateView.as_view(template_name='ReviewProblemSample/review_problem_sample_all.html'), name='review_problem_sample_all'),
    # path('documents/reviews/review_document_consent', TemplateView.as_view(template_name='ReviewProblemDocument/review_problem_document_consent_all.html'), name='review_problem_document_consent_all'),

    path('documents/reviews/review_sample/new',
         ReviewProblemSampleCreateView.as_view(),
         name='review_problem_sample_new'),
    path('documents/reviews/review_document_consent/new',
         ReviewProblemDocumentConsentCreateView.as_view(),
         name='review_problem_document_consent_new'),

    path('documents/reviews/review_sample/success',
         TemplateView.as_view(template_name='ReviewProblemSample/review_problem_sample_success.html'),
         name='review_problem_sample_success'),

    path('documents/reviews/review_document_consent/success',
         TemplateView.as_view(template_name='ReviewProblemDocument/review_problem_document_consent_success.html'),
         name='review_problem_document_consent_success'),

    path('documents/sign', TemplateView.as_view(template_name='document_sign/document_sign_all.html'), name='documents_sign_all'),
    path('documents/sign/dc', SignDocumentListView.as_view(), name='sign_dc_all'),
    path('documents/sign/dc/new', SignDocumentCreateView.as_view(), name='sign_dc_new'),

    path('documents/sign/dc/<int:pk>/', SignDocumentDetailView.as_view(), name='sign_dc_detail'),
    path('documents/sign/dc/<int:pk>/delete', SignDocumentDeleteView.as_view(), name='sign_dc_delete'),




    path('documents/head/sign', TemplateView.as_view(template_name='document_sign/head_sign_dc/head_document_sign_all.html'), name='head_documents_sign_all'),
    path('documents/head/sign/dc', HeadSignDocumentListView.as_view(), name='head_sign_dc_all'),
    path('documents/head/sign/dc/new', HeadSignDocumentCreateView.as_view(), name='head_sign_dc_new'),

    path('documents/head/sign/dc/<int:pk>/', HeadSignDocumentDetailView.as_view(), name='head_sign_dc_detail'),
    path('documents/head/sign/dc/<int:pk>/edit', HeadSignDocumentUpdateView.as_view(), name='head_sign_dc_detail_edit'),


    # path('documents/sign/docpack/new', TemplateView.as_view(template_name='document_sign/head_document_sign_all.html'),
    #      name='documents_sign_all'),

]