# Generated by Django 5.0.3 on 2024-03-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_document_template_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
            ],
        ),
    ]