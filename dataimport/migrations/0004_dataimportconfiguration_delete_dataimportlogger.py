# Generated by Django 5.1rc1 on 2024-10-15 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataimport', '0003_dataimportlogger'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataImportConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_data_import', models.DateTimeField(blank=True, null=True, verbose_name='Data')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('github_url_for_import_data', models.URLField(blank=True, null=True, verbose_name='Github URL for import data')),
            ],
            options={
                'verbose_name': 'Logger import data from GitHub',
                'verbose_name_plural': 'Loggers import data from GitHub',
                'ordering': ['last_data_import'],
            },
        ),
        migrations.DeleteModel(
            name='DataImportLogger',
        ),
    ]