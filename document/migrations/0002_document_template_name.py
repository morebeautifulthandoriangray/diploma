# Generated by Django 5.0.3 on 2024-03-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='template_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
