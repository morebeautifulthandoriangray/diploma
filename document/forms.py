from .models import Sample, DocumentConsent, DocumentNotification
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

class DocumentNotificationForm(ModelForm):
    class Meta:
        model = DocumentNotification
        fields = [
            'title',
            'template_name',

            'program_name',
            'program_destiny',

            # руководитель
            'head_name',
            'head_surname' ,
            'head_patronomic',

            'applicant1_name',
            'applicant1_surname' ,
            'applicant1_patronomic',

            'applicant2_name',
            'applicant2_surname',
            'applicant2_patronomic',

            'applicant1_uni_position',
            'applicant2_uni_position',

            'uni_department',

            'applicant1_index',
            'applicant1_country',
            'applicant1_city',
            'applicant1_street',
            'applicant1_build_number',
            'applicant1_flat_number',
            'applicant1_snils',

            'applicant2_index',
            'applicant2_country' ,
            'applicant2_city',
            'applicant2_street',
            'applicant2_build_number' ,
            'applicant2_flat_number' ,
            'applicant2_snils' ,

            'applicant1_percent_contribution' ,
            'applicant2_percent_contribution' ,

            'applicant1_phone_number' ,
            'applicant2_phone_number',

            'applicant1_email',
            'applicant2_email',
            'program_usage',
            'fee',
    ]
