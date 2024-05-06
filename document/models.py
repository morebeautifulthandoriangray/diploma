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
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    path_to_template = models.FileField(blank=True)
    program_name = models.CharField(max_length=500)
    application_number = models.IntegerField(null=True)
    main_applicant_name = models.CharField(max_length=200)
    main_applicant_surname = models.CharField(max_length=200)
    main_applicant_patronomic = models.CharField(max_length=200)
    second_applicant_name = models.CharField(max_length=200)
    second_applicant_surname = models.CharField(max_length=200)
    second_applicant_patronomic = models.CharField(max_length=200)
    second_applicant_date_of_birth = models.DateField(null=True)
    address_index = models.IntegerField(null=True)
    # подсказка - указать для пользователя, что нужно вводить полное название страны - Российская федерация
    address_country = models.CharField(max_length=200)
    address_city = models.CharField(max_length=200)
    address_street = models.CharField(max_length=200)
    address_building_number = models.SmallIntegerField(null=True)
    address_house_flat_number = models.SmallIntegerField(null=True)
    current_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('document_consent_detail', args=[str(self.id)],)
