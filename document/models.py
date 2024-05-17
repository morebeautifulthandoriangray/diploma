from django.db import models
from django.db.models import Model
from django.urls import reverse
from django import forms
from diploma import settings
from django.core.validators import RegexValidator

class RussianPhoneNumber(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10,11}$', message="Phone number must be entered in the format: '+79991234567'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True)

    def __str__(self):
        return self.phone_number

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE)
    path_to_doc = models.FileField(blank=True)

    def __str__(self):
        return self.title


class Sample(Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    path_to_template = models.FileField(blank=True, upload_to='upload_sample/%Y-%m-%d/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sample_detail', args=[str(self.id)], )

    class Meta:
        ordering = ('-created_at',)


class DocumentConsent(Model):
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10,11}$',
                                 message="Phone number must be entered in the format: '+79991234567'. Up to 11 digits allowed.")
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE)
    path_to_template = models.FileField(blank=True)
    program_name = models.CharField(max_length=500)
    application_number = models.IntegerField(null=True)
    applicant_name = models.CharField(max_length=200)
    applicant_surname = models.CharField(max_length=200)
    applicant_patronomic = models.CharField(max_length=200)
    applicant_date_of_birth = models.DateField(null=True)
    address_index = models.IntegerField(null=True)
    address_country = models.CharField(max_length=200)
    address_city = models.CharField(max_length=200)
    address_street = models.CharField(max_length=200)
    address_building_number = models.SmallIntegerField(null=True)
    address_house_flat_number = models.SmallIntegerField(null=True)
    applicant_phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True, default='+79998887716')
    current_date = models.DateField(auto_now=True)
    # applicant_name_short = applicant_name[0]
    # applicant_patronomic_short = applicant_patronomic[0]
    passport_seria = models.IntegerField(null=True)
    passport_number = models.IntegerField(null=True)
    passport_date_of_issue = models.DateField(null=True)
    passport_place_giving = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document_consent_detail', args=[str(self.id)], )
    # подсказка - указать для пользователя, что нужно вводить полное название страны - Российская федерация


class DocumentNotification(Model):
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10,11}$',
                                 message="Phone number must be entered in the format: '+79991234567'. Up to 11 digits allowed.")
    title = models.CharField(max_length=200)
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE)
    path_to_template = models.FileField(blank=True)

    program_name = models.CharField(max_length=500, blank=True)
    program_destiny = models.CharField(max_length=500, blank=True)

    # руководитель
    head_name = models.CharField(max_length=200, blank=True)
    head_surname = models.CharField(max_length=200, blank=True)
    head_patronomic = models.CharField(max_length=200, blank=True)


    applicant1_name = models.CharField(max_length=200, blank=True)
    applicant1_surname = models.CharField(max_length=200, blank=True)
    applicant1_patronomic = models.CharField(max_length=200, blank=True)

    applicant2_name = models.CharField(max_length=200, blank=True)
    applicant2_surname = models.CharField(max_length=200, blank=True)
    applicant2_patronomic = models.CharField(max_length=200, blank=True)

    applicant1_uni_position = models.CharField(max_length=200, blank=True)
    applicant2_uni_position = models.CharField(max_length=200, blank=True)

    uni_department = models.CharField(max_length=20, blank=True)


    applicant1_index = models.IntegerField(null=True)
    applicant1_country = models.CharField(max_length=200, blank=True)
    applicant1_city = models.CharField(max_length=200, blank=True)
    applicant1_street = models.CharField(max_length=200, blank=True)
    applicant1_build_number = models.SmallIntegerField(null=True)
    applicant1_flat_number = models.SmallIntegerField(null=True)
    applicant1_snils = models.CharField(max_length=200, blank=True)

    applicant2_index = models.IntegerField(null=True, blank=True)
    applicant2_country = models.CharField(max_length=200, blank=True)
    applicant2_city = models.CharField(max_length=200, blank=True)
    applicant2_street = models.CharField(max_length=200, blank=True)
    applicant2_build_number = models.SmallIntegerField(null=True, blank=True)
    applicant2_flat_number = models.SmallIntegerField(null=True, blank=True)
    applicant2_snils = models.CharField(max_length=200, blank=True)

    applicant1_percent_contribution = models.SmallIntegerField(null=True)
    applicant2_percent_contribution = models.SmallIntegerField(null=True)

    applicant1_phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True, default='+79998887716')
    applicant2_phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True, default='+79998887716')

    applicant1_email = models.CharField(max_length=200, blank=True)
    applicant2_email = models.CharField(max_length=200, blank=True)

    program_usage = models.CharField(max_length=200, blank=True)

    fee = models.SmallIntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    current_date = models.DateField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document_notification_detail', args=[str(self.id)], )


class DocumentAuthorsAward(Model):
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10,11}$',
                                 message="Phone number must be entered in the format: '+79991234567'. Up to 11 digits allowed.")
    title = models.CharField(max_length=200)
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE)
    path_to_template = models.FileField(blank=True)

    program_name = models.CharField(max_length=500, blank=True)

    # 1
    applicant1_name = models.CharField(max_length=200, blank=True)
    applicant1_surname = models.CharField(max_length=200, blank=True)
    applicant1_patronomic = models.CharField(max_length=200, blank=True)
    applicant1_date_birth = models.DateField(null=True)

    applicant1_passport_seria = models.IntegerField(null=True)
    applicant1_passport_number = models.IntegerField(null=True)
    applicant1_passport_date_of_issue = models.DateField(null=True)
    applicant1_passport_place_giving = models.CharField(max_length=500, null=True)

    applicant1_inn = models.CharField(max_length=200, blank=True)
    applicant1_snils = models.CharField(max_length=200, blank=True)
    applicant1_bank_info = models.CharField(max_length=200, blank=True)
    applicant1_account_number = models.CharField(max_length=200, blank=True)
    applicant1_bik = models.CharField(max_length=200, blank=True)
    applicant1_bank_inn = models.CharField(max_length=200, blank=True)
    applicant1_bank_kpp = models.CharField(max_length=200, blank=True)
    applicant1_corr_account = models.CharField(max_length=200, blank=True)


    # 2
    applicant2_name = models.CharField(max_length=200, blank=True)
    applicant2_surname = models.CharField(max_length=200, blank=True)
    applicant2_patronomic = models.CharField(max_length=200, blank=True)
    applicant2_date_birth = models.DateField(null=True)


    applicant2_passport_seria = models.IntegerField(null=True)
    applicant2_passport_number = models.IntegerField(null=True)
    applicant2_passport_date_of_issue = models.DateField(null=True)
    applicant2_passport_place_giving = models.CharField(max_length=500, null=True)

    applicant2_inn = models.CharField(max_length=200, blank=True)
    applicant2_snils = models.CharField(max_length=200, blank=True)
    applicant2_bank_info = models.CharField(max_length=200, blank=True)
    applicant2_account_number = models.CharField(max_length=200, blank=True)
    applicant2_bik = models.CharField(max_length=200, blank=True)
    applicant2_bank_inn = models.CharField(max_length=200, blank=True)
    applicant2_bank_kpp = models.CharField(max_length=200, blank=True)
    applicant2_corr_account = models.CharField(max_length=200, blank=True)


    authors_award = models.SmallIntegerField(null=True, blank=True)

    # не хочется делать эту логику делания на 2 на беке, мб на фронте сделать?
    # applicant1_authors_award = models.SmallIntegerField(null=True, blank=True)
    # applicant2_authors_award = models.SmallIntegerField(null=True, blank=True)

    # authors_award_text - не забыть это подсчитать с помощью спец библиотеки нам ту текст
    # applicant1_name_short
    # applicant1_patronomic_short
    #applicant2_name_short
    #applicant2_patronomic_short
    #
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document_authors_award_detail', args=[str(self.id)], )