# Generated by Django 5.0.3 on 2024-05-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0018_documentauthorsaward'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentauthorsaward',
            name='program_name',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
