from django.db import models
from django.db.models import Model
from django.urls import reverse
from django import forms
from diploma import settings
from django.core.validators import RegexValidator
from django_prometheus.models import ExportModelOperationsMixin

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

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Sample(ExportModelOperationsMixin('sample'), Model):
    title = models.CharField(max_length=200, verbose_name='Название шаблона')
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Дата создания')
    path_to_template = models.FileField(blank=True, upload_to='upload_sample/%Y-%m-%d/', verbose_name='Путь до файла')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sample_detail', args=[str(self.id)], )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'


class DocumentConsent(ExportModelOperationsMixin('consent'), Model):
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10,11}$',
                                 message="Phone number must be entered in the format: '+79991234567'. Up to 11 digits allowed.")
    title = models.CharField(max_length=200, verbose_name='Название документа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Имя шаблона')
    path_to_template = models.FileField(blank=True, verbose_name='Путь до документа', upload_to='download_document/consent/%Y-%m-%d/')
    program_name = models.CharField(max_length=500, verbose_name='Название программы')
    application_number = models.IntegerField(null=True, verbose_name='Номер заявки')
    applicant_name = models.CharField(max_length=200, verbose_name='Имя заявителя')
    applicant_surname = models.CharField(max_length=200, verbose_name='Фамилия заявителя')
    applicant_patronomic = models.CharField(max_length=200 , verbose_name='Отчество заявителя')
    applicant_date_of_birth = models.DateField(null=True, verbose_name='Дата рождения заявителя')
    address_index = models.IntegerField(null=True, verbose_name='Индекс здания')
    address_country = models.CharField(max_length=200, verbose_name='Страна')
    address_city = models.CharField(max_length=200, verbose_name='Город')
    address_street = models.CharField(max_length=200 , verbose_name='Улица')
    address_building_number = models.SmallIntegerField(null=True, verbose_name='Номер дома')
    address_house_flat_number = models.SmallIntegerField(null=True, verbose_name='Номер квартиры')
    applicant_phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True, default='+79998887716', verbose_name='Номер телефона заявителя')
    current_date = models.DateField(auto_now=True)
    # applicant_name_short = applicant_name[0]
    # applicant_patronomic_short = applicant_patronomic[0]
    passport_seria = models.IntegerField(null=True, verbose_name='Серия паспорта заявителя')
    passport_number = models.IntegerField(null=True, verbose_name='Номер паспорта заявителя')
    passport_date_of_issue = models.DateField(null=True, verbose_name='Дата выдачи паспорта')
    passport_place_giving = models.CharField(max_length=500, null=True, verbose_name='Кем выдан паспорт')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document_consent_detail', args=[str(self.id)], )
    # подсказка - указать для пользователя, что нужно вводить полное название страны - Российская федерация

    class Meta:
        verbose_name = 'Документ согласие на персональные данные'
        verbose_name_plural = 'Документы согласие на персональные данные'
        ordering = ('-created_at',)



class DocumentNotification(Model):
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10,11}$',
                                 message="Phone number must be entered in the format: '+79991234567'. Up to 11 digits allowed.")
    title = models.CharField(max_length=200, verbose_name='Название документа')
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Имя шаблона')
    path_to_template = models.FileField(blank=True, verbose_name='Путь до шаблона')

    program_name = models.CharField(max_length=500, blank=True, verbose_name='Название программы')
    program_destiny = models.CharField(max_length=500, blank=True, verbose_name='Назначение программы')

    # руководитель
    head_name = models.CharField(max_length=200, blank=True, verbose_name='Имя руководителя')
    head_surname = models.CharField(max_length=200, blank=True, verbose_name='Фамилия руководителя')
    head_patronomic = models.CharField(max_length=200, blank=True, verbose_name='Отчество руководителя')


    applicant1_name = models.CharField(max_length=200, blank=True, verbose_name='Имя заявителя 1')
    applicant1_surname = models.CharField(max_length=200, blank=True, verbose_name='Фамилия заявителя 1')
    applicant1_patronomic = models.CharField(max_length=200, blank=True, verbose_name='Отчество заявителя 1')

    applicant2_name = models.CharField(max_length=200, blank=True, verbose_name='Имя заявителя 2')
    applicant2_surname = models.CharField(max_length=200, blank=True, verbose_name='Фамилия заявителя 2')
    applicant2_patronomic = models.CharField(max_length=200, blank=True , verbose_name='Отчество заявителя 2')

    applicant1_uni_position = models.CharField(max_length=200, blank=True, verbose_name='Должность в университете заявителя 1')
    applicant2_uni_position = models.CharField(max_length=200, blank=True, verbose_name='Должность в университете заявителя 2')

    uni_department = models.CharField(max_length=20, blank=True, verbose_name='Кафедра университета')


    applicant1_index = models.IntegerField(null=True, verbose_name='Индекс здания заявителя 1')
    applicant1_country = models.CharField(max_length=200, blank=True, verbose_name='Страна заявителя 1')
    applicant1_city = models.CharField(max_length=200, blank=True, verbose_name='Город заявителя 1')
    applicant1_street = models.CharField(max_length=200, blank=True, verbose_name='Улица заявителя 1')
    applicant1_build_number = models.SmallIntegerField(null=True, verbose_name='Номер здания заявителя 1')
    applicant1_flat_number = models.SmallIntegerField(null=True, verbose_name='Номер квартиры заявителя 1')
    applicant1_snils = models.CharField(max_length=200, blank=True, verbose_name='СНИЛС заявителя 1')

    applicant2_index = models.IntegerField(null=True, blank=True, verbose_name='Индекс здания заявителя 2')
    applicant2_country = models.CharField(max_length=200, blank=True, verbose_name='Страна заявителя 2')
    applicant2_city = models.CharField(max_length=200, blank=True, verbose_name='Город заявителя 2')
    applicant2_street = models.CharField(max_length=200, blank=True, verbose_name='Улица заявителя 2')
    applicant2_build_number = models.SmallIntegerField(null=True, blank=True, verbose_name='Номер здания заявителя 2')
    applicant2_flat_number = models.SmallIntegerField(null=True, blank=True, verbose_name='Номер квартиры заявителя 2')
    applicant2_snils = models.CharField(max_length=200, blank=True, verbose_name='Номер квартиры заявителя 2')

    applicant1_percent_contribution = models.SmallIntegerField(null=True, verbose_name='Процент вклада заявителя 1')
    applicant2_percent_contribution = models.SmallIntegerField(null=True, verbose_name='Процент вклада заявителя 2')

    applicant1_phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True, default='+79998887716' , verbose_name='Номер телефона заявителя 1')
    applicant2_phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True, default='+79998887716', verbose_name='Номер телефона заявителя 2')

    applicant1_email = models.CharField(max_length=200, blank=True, verbose_name='Email заявителя 1')
    applicant2_email = models.CharField(max_length=200, blank=True, verbose_name='Email заявителя 2')

    program_usage = models.CharField(max_length=200, blank=True, verbose_name='Где может быть использована программа')

    fee = models.SmallIntegerField(null=True, verbose_name='Пошлина в размере')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    current_date = models.DateField(auto_now=True, verbose_name='Текущая дата')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document_notification_detail', args=[str(self.id)], )


    class Meta:
        verbose_name = 'Документ на уведомление'
        verbose_name_plural = 'Документы на уведомление'
        ordering = ('-created_at',)



class DocumentAuthorsAward(Model):
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10,11}$',
                                 message="Phone number must be entered in the format: '+79991234567'. Up to 11 digits allowed.")
    title = models.CharField(max_length=200, verbose_name='Название документа')
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Имя шаблона')
    path_to_template = models.FileField(blank=True, verbose_name='Путь до шаблона')

    program_name = models.CharField(max_length=500, blank=True, verbose_name='Название программы')

    # 1
    applicant1_name = models.CharField(max_length=200, blank=True, verbose_name='Имя заявителя 1')
    applicant1_surname = models.CharField(max_length=200, blank=True, verbose_name='Фамилия заявителя 1')
    applicant1_patronomic = models.CharField(max_length=200, blank=True, verbose_name='Отчество заявителя 1')
    applicant1_date_birth = models.DateField(null=True, verbose_name='Дата рождения заявителя 1')

    applicant1_passport_seria = models.IntegerField(null=True, verbose_name='Серия паспорта заявителя 1')
    applicant1_passport_number = models.IntegerField(null=True, verbose_name='Номер паспорта заявителя 1')
    applicant1_passport_date_of_issue = models.DateField(null=True, verbose_name='Дата выдачи паспорта заявителя 1')
    applicant1_passport_place_giving = models.CharField(max_length=500, null=True, verbose_name='Кем выдан паспорт заявителя 1')

    applicant1_inn = models.CharField(max_length=200, blank=True, verbose_name='ИНН заявителя 1')
    applicant1_snils = models.CharField(max_length=200, blank=True, verbose_name='СНИЛС заявителя 1')
    applicant1_bank_info = models.CharField(max_length=200, blank=True, verbose_name='Банк заявителя 1')
    applicant1_account_number = models.CharField(max_length=200, blank=True, verbose_name='Номер счета заявителя 1')
    applicant1_bik = models.CharField(max_length=200, blank=True, verbose_name='БИК заявителя 1')
    applicant1_bank_inn = models.CharField(max_length=200, blank=True, verbose_name='ИНН Банка заявителя 1')
    applicant1_bank_kpp = models.CharField(max_length=200, blank=True, verbose_name='КПП Банка заявителя 1')
    applicant1_corr_account = models.CharField(max_length=200, blank=True, verbose_name='Кор. счет заявителя 1')


    # 2
    applicant2_name = models.CharField(max_length=200, blank=True, verbose_name='Имя заявителя 2')
    applicant2_surname = models.CharField(max_length=200, blank=True, verbose_name='Фамилия заявителя 2')
    applicant2_patronomic = models.CharField(max_length=200, blank=True, verbose_name='Отчество заявителя 2')
    applicant2_date_birth = models.DateField(null=True, verbose_name='Дата рождения заявителя 2')


    applicant2_passport_seria = models.IntegerField(null=True, verbose_name='Серия паспорта заявителя 2')
    applicant2_passport_number = models.IntegerField(null=True, verbose_name='Номер паспорта заявителя 2')
    applicant2_passport_date_of_issue = models.DateField(null=True, verbose_name='Дата выдачи паспорта заявителя 2')
    applicant2_passport_place_giving = models.CharField(max_length=500, null=True, verbose_name='Кем выдан паспорт заявителя 2')

    applicant2_inn = models.CharField(max_length=200, blank=True, verbose_name='ИНН заявителя 2')
    applicant2_snils = models.CharField(max_length=200, blank=True, verbose_name='СНИЛС заявителя 2')
    applicant2_bank_info = models.CharField(max_length=200, blank=True, verbose_name='Банк заявителя 2')
    applicant2_account_number = models.CharField(max_length=200, blank=True, verbose_name='Номер счета заявителя 2')
    applicant2_bik = models.CharField(max_length=200, blank=True, verbose_name='БИК заявителя 2')
    applicant2_bank_inn = models.CharField(max_length=200, blank=True, verbose_name='ИНН Банка заявителя 2')
    applicant2_bank_kpp = models.CharField(max_length=200, blank=True, verbose_name='КПП Банка заявителя 2')
    applicant2_corr_account = models.CharField(max_length=200, blank=True, verbose_name='Кор. счет заявителя 2')


    authors_award = models.SmallIntegerField(null=True, blank=True, verbose_name='Сумма вознаграждения')

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

    class Meta:
        verbose_name = 'Документ на авт.вознаграждение'
        verbose_name_plural = 'Документы на авт.вознаграждение'
        # ordering = ('-created_at',)




class DocumentDiplomaPractice(Model):
    title = models.CharField(max_length=200)
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE)
    path_to_template = models.FileField(blank=True)

    student_name = models.CharField(max_length=200, blank=True)
    student_surname = models.CharField(max_length=200, blank=True)
    student_patronomic = models.CharField(max_length=200, blank=True)

    org_name = models.CharField(max_length=200, blank=True)
    org_surname = models.CharField(max_length=200, blank=True)
    org_patronomic = models.CharField(max_length=200, blank=True)


    # _shorrt
    # student_name = models.CharField(max_length=200, blank=True)
    # student_patronomic = models.CharField(max_length=200, blank=True)

    # org_name = models.CharField(max_length=200, blank=True)
    # org_patronomic = models.CharField(max_length=200, blank=True)

    practice_company = models.CharField(max_length=200, blank=True)
    practice_address = models.CharField(max_length=200, blank=True)
    practice_date_from = models.DateField(null=True)
    practice_date_to = models.DateField(null=True)

    agreement_number = models.CharField(max_length=200, blank=True)
    date_agreement = models.DateField(null=True)


class DocumentSACB(Model):
    title = models.CharField(max_length=200)
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE)
    path_to_template = models.FileField(blank=True)

    project_sponsor = models.CharField(max_length=200, blank=True)
    project_name = models.CharField(max_length=200, blank=True)
    project_developer = models.CharField(max_length=200, blank=True)
    project_purpose = models.CharField(max_length=200, blank=True)
    project_tasks = models.CharField(max_length=500, blank=True)
    project_deadline = models.DateField(auto_now=True)
    project_participants = models.CharField(max_length=200, blank=True)
    project_short_description = models.CharField(max_length=200, blank=True)
    projects_integration = models.CharField(max_length=200, blank=True)
    expected_final_results = models.CharField(max_length=200, blank=True)
    project_financing_sources = models.CharField(max_length=200, blank=True)

    current_date = models.DateField(auto_now=True)


class DocumentSet(Model):
    title = models.CharField(max_length=200, verbose_name='Название пакета')
    template_name = models.ForeignKey('Sample', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Имя шаблона')
    document_consent = models.ForeignKey('DocumentConsent', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Документ об согласие на обработку персональных данных')
    document_notification = models.ForeignKey('DocumentNotification', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Документ об согласии на уведомление об регистрации')
    document_authors_award = models.ForeignKey('DocumentAuthorsAward', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Документ на авторское вознаграждение')

    current_date = models.DateField(auto_now=True, verbose_name='Текущая дата')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document_set_detail', args=[str(self.id)], )


    class Meta:
        verbose_name = 'Пакет документов'
        verbose_name_plural = 'Пакеты документов'
        ordering = ('-created_at',)





