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
from docx2pdf import convert
from docxtpl import DocxTemplate


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
    fields = ['title', 'template_name', 'path_to_template', 'program_name', 'application_number', 'applicant_name',
              'applicant_surname',
              'applicant_patronomic',
              'applicant_date_of_birth',
              'address_index',
              'address_country',
              'address_city',
              'address_street',
              'address_building_number',
              'address_house_flat_number', 'passport_seria', 'passport_number', 'passport_date_of_issue',  'passport_place_giving']

    path_to_template = model.path_to_template



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



class DocumentConsentDownloadDocx(View):
    def get(self, request, pk=1, *args, **kwargs):
        document_consent_program_name = DocumentConsent.objects.get(pk=pk).program_name
        document_consent_application_number = DocumentConsent.objects.get(pk=pk).application_number
        document_consent_applicant_name = DocumentConsent.objects.get(pk=pk).application_number
        document_consent_applicant_surname = DocumentConsent.objects.get(pk=pk).applicant_surname
        document_consent_applicant_patronomic = DocumentConsent.objects.get(pk=pk).applicant_patronomic
        document_consent_applicant_date_of_birth = DocumentConsent.objects.get(pk=pk).applicant_date_of_birth
        document_consent_address_index = DocumentConsent.objects.get(pk=pk).address_index
        document_consent_address_country = DocumentConsent.objects.get(pk=pk).address_country
        document_consent_address_city = DocumentConsent.objects.get(pk=pk).address_city
        document_consent_address_street = DocumentConsent.objects.get(pk=pk).address_street
        document_consent_address_building_number = DocumentConsent.objects.get(pk=pk).address_building_number
        document_consent_address_house_flat_number = DocumentConsent.objects.get(pk=pk).address_house_flat_number
        document_consent_current_date = DocumentConsent.objects.get(pk=pk).current_date
        document_consent_passport_seria = DocumentConsent.objects.get(pk=pk).passport_seria
        document_consent_passport_number = DocumentConsent.objects.get(pk=pk).passport_number
        document_consent_passport_date_of_issue = DocumentConsent.objects.get(pk=pk).passport_date_of_issue
        document_consent_passport_place_giving = DocumentConsent.objects.get(pk=pk).passport_place_giving

        file_path = '/Users/keito/Programming/Python/train/diploma/media/upload_sample/2024-05-02/sogsasiebro1.docx'
            # os.path.join(settings.MEDIA_ROOT, '/upload_sample/2024-05-02/sogsasiebro1.docx')  # Specify the path to your file
        if file_path.endswith('.docx'):
            doc = DocxTemplate(file_path)
            context = {
                'program_name': document_consent_program_name,
                'application_number': document_consent_application_number,
                'applicant_name': document_consent_applicant_name,
                'applicant_surname': document_consent_applicant_surname,
                'applicant_patronomic': document_consent_applicant_patronomic,
                'applicant_date_of_birth': document_consent_applicant_date_of_birth,
                'address_index': document_consent_address_index,
                'address_country': document_consent_address_country,
                'address_city': document_consent_address_city,
                'address_street': document_consent_address_street,
                'address_building_number': document_consent_address_building_number,
                'address_house_flat_number': document_consent_address_house_flat_number,
                'current_date': document_consent_current_date,
                'applicant_name_short': document_consent_applicant_name,
                'applicant_patronomic_short': document_consent_applicant_patronomic,
                'passport_seria': document_consent_passport_seria,
                'passport_number': document_consent_passport_number,
                'passport_date_of_issue': document_consent_passport_date_of_issue,
                'passport_place_giving': document_consent_passport_place_giving,
            }
            doc.render(context)
            file_name = 'downloaded_file.docx'
            doc.save(file_name)
            # file_name = 'downloaded_file.docx'
        # elif file_path.endswith('.pdf'):
        #     file_name_1 = 'downloaded_file.pdf'
        #     file_name = convert(file_path, file_name_1)
        # else:
        #     return HttpResponseBadRequest('Unsupported file format. Only DOCX and PDF files are allowed.'
        #
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
        # sample = Sample.objects.get(pk=pk).path_to_template
        # file_path = os.path.join(settings.MEDIA_ROOT, f'{sample}')  # Specify the path to your file
        # if file_path.endswith('.docx'):
        #     file_name = 'downloaded_file.docx'
        # # elif file_path.endswith('.pdf'):
        # #     file_name_1 = 'downloaded_file.pdf'
        # #     file_name = convert(file_path, file_name_1)
        # # else:
        # #     return HttpResponseBadRequest('Unsupported file format. Only DOCX and PDF files are allowed.'
        # #
        # response = FileResponse(open(file_path, 'rb'))
        # response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        # return response


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
        # elif file_path.endswith('.pdf'):
        #     file_name_1 = 'downloaded_file.pdf'
        #     file_name = convert(file_path, file_name_1)
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
            file_name_1 = 'downloaded_file.docx'
            file_name = convert(file_path, file_name_1)
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




