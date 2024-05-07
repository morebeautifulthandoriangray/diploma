from .models import Sample, DocumentConsent
from django.forms import ModelForm
from django import forms
from diploma import settings

class SampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = ['title', 'path_to_template']


class DocumentConsentForm(ModelForm):
    class Meta:
        model = DocumentConsent
        fields = ['title',
                  # 'created_at',
                  'template_name',
                  'program_name',
                  'application_number',
                  'applicant_name',
                  'applicant_surname',
                  'applicant_patronomic',
                  'applicant_date_of_birth',
                  'address_index',
                  'address_country',
                  'address_city',
                  'address_street',
                  'address_building_number',
                  'address_house_flat_number',
                  'applicant_phone_number',
                  # 'current_date',
                  'passport_seria',
                  'passport_number',
                  'passport_date_of_issue',
                  'passport_place_giving'
                  ]
        # applicant_date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        # current_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        # passport_date_of_issue = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    applicant_date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        # current_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    passport_date_of_issue = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    application_number = forms.IntegerField(help_text='Указывается при наличии регистрационного номера заявки')
