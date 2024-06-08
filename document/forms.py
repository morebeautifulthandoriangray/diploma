from .models import Sample, DocumentConsent, DocumentNotification, DocumentAuthorsAward, DocumentSet, \
    ReviewProblemSample, ReviewProblemDocumentConsent, SignDocument
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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }

    title = forms.CharField(max_length=100, required=True, label='Название документа')
    applicant_name = forms.CharField(max_length=100, required=True, label='Имя заявителя')
    applicant_date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, label='Дата рождения заявителя')
        # current_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    passport_date_of_issue = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, label='Дата выдачи паспорта')
    application_number = forms.IntegerField(help_text='Указывается при наличии регистрационного номера заявки', label='Номер заявки')


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


class DocumentAuthorsAwardForm(ModelForm):
    class Meta:
        model = DocumentAuthorsAward
        fields = [
            'title',
            'template_name',

            'program_name',

            'applicant1_name' ,
            'applicant1_surname' ,
            'applicant1_patronomic' ,
            'applicant1_date_birth' ,

            'applicant1_passport_seria' ,
            'applicant1_passport_number' ,
            'applicant1_passport_date_of_issue' ,
            'applicant1_passport_place_giving' ,

            'applicant1_inn' ,
            'applicant1_snils' ,
            'applicant1_bank_info' ,
            'applicant1_account_number',
            'applicant1_bik',
            'applicant1_bank_inn',
            'applicant1_bank_kpp' ,
            'applicant1_corr_account',

            # 2
            'applicant2_name',
            'applicant2_surname',
            'applicant2_patronomic',
            'applicant2_date_birth',

            'applicant2_passport_seria',
            'applicant2_passport_number',
            'applicant2_passport_date_of_issue',
            'applicant2_passport_place_giving',

            'applicant2_inn',
            'applicant2_snils',
            'applicant2_bank_info',
            'applicant2_account_number',
            'applicant2_bik',
            'applicant2_bank_inn',
            'applicant2_bank_kpp' ,
            'applicant2_corr_account',

            'authors_award',


        ]

    applicant1_date_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    applicant2_date_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    # current_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    applicant1_passport_date_of_issue = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    applicant2_passport_date_of_issue = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)


class DocumentSetForm(ModelForm):
    class Meta:
        model = DocumentSet

        fields = ['title',
                  'template_name',
                  'document_consent',
                  'document_notification',
                  'document_authors_award']

class ReviewProblemSampleForm(ModelForm):
    class Meta:
        model = ReviewProblemSample

        fields = ['review_problem_sample_title',
                  'sample_name',
                  'review_text']


class ReviewProblemDocumentConsentForm(ModelForm):
    class Meta:
        model = ReviewProblemDocumentConsent

        fields = ['review_problem_document_consent_title',
                  'document_consent_name',
                  'review_text']



class SignDocumentForm(ModelForm):
    class Meta:
        model = SignDocument

        fields = [
                  'document_consent_name',
            'FIO_head',
                  'status']

    # document_consent_name = forms.CharField(emp)

class HeadSignDocumentForm(ModelForm):
    class Meta:
        model = SignDocument

        fields = [
            'status']

        # document_consent_name = forms.CharField(emp)