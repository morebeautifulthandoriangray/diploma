# Generated by Django 5.0.3 on 2024-03-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_d'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('path_to_template', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='D',
        ),
    ]
