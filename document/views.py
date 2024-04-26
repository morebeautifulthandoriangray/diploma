from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Document
from pydocx import PyDocX
from .models import Document, DocumentConsent, Sample
from .forms import SampleForm
from django.views.generic.base import View
from django.http import FileResponse
from django.conf import settings
import os
from django.http import HttpResponse, HttpResponseBadRequest


# Create your views here.


# class DocumentListView(ListView):
#     model = Document
#     template_name = 'documents_all.html'


class DocumentConsentListView(ListView):
    model = DocumentConsent
    template_name = 'documents_consent_all.html'


class DocumentConsentCreateView(CreateView):
    model = DocumentConsent
    template_name = 'documents_consent_new.html'
    fields = ['title', 'path_to_template', 'program_name', 'application_number', 'applicant_name',
              'applicant_surname',
              'applicant_patronomic',
              'applicant_date_of_birth',
              'address_index',
              'address_country',
              'address_city',
              'address_street',
              'address_building_number',
              'address_house_flat_number']


class DocumentConsentDetailView(DetailView):
    model = DocumentConsent
    template_name = 'document_consent_detail.html'


class DocumentConsentUpdateView(UpdateView):
    model = DocumentConsent
    template_name = 'document_consent_edit.html'
    fields = ['title', 'path_to_template', 'program_name', 'application_number', 'applicant_name',
              'applicant_surname',
              'applicant_patronomic',
              'applicant_date_of_birth',
              'address_index',
              'address_country',
              'address_city',
              'address_street',
              'address_building_number',
              'address_house_flat_number']


class DocumentConsentDeleteView(DeleteView):
    model = DocumentConsent
    template_name = 'document_consent_delete.html'
    success_url = reverse_lazy('documents_consent_all')


class SampleListView(ListView):
    model = Sample
    template_name = 'samples_list.html'


class SampleDetailView(DetailView):
    model = Sample
    template_name = 'sample_detail.html'

class FileDownloadDocx(View):
    def get(self, request, pk=1, *args, **kwargs):
        sample = Sample.objects.get(pk=pk).path_to_template
        file_path = os.path.join(settings.MEDIA_ROOT, f'{sample}')  # Specify the path to your file
        if file_path.endswith('.docx'):
            file_name = 'downloaded_file.docx'
        elif file_path.endswith('.pdf'):
            file_name = 'downloaded_file.pdf'
        # else:
        #     return HttpResponseBadRequest('Unsupported file format. Only DOCX and PDF files are allowed.'
        #
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response

class FileDownloadPdf(View):
    def get(self, request, pk=1, *args, **kwargs):
        sample = Sample.objects.get(pk=pk).path_to_template
        file_path = os.path.join(settings.MEDIA_ROOT, f'{sample}')  # Specify the path to your file
        if file_path.endswith('.docx'):
            file_name = 'downloaded_file.docx'
        elif file_path.endswith('.pdf'):
            file_name = 'downloaded_file.pdf'
        # else:
        #     return HttpResponseBadRequest('Unsupported file format. Only DOCX and PDF files are allowed.'
        #
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response

class SampleCreateView(CreateView):
    model = Sample
    form_class = SampleForm
    template_name = 'sample_new.html'


    # fields = ['title', 'path_to_template']
    success_url = reverse_lazy('samples_all')


class SampleUpdateView(UpdateView):
    model = Sample
    form_class = SampleForm
    template_name = 'sample_edit.html'
    # fields = ['title', 'path_to_template']


class SampleDeleteView(DeleteView):
    model = Sample
    template_name = 'sample_delete.html'
    success_url = reverse_lazy('samples_all')




