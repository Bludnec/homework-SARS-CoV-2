# Generated by Django 5.1rc1 on 2024-10-17 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataimport', '0005_alter_dataimportconfiguration_github_url_for_import_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataimportconfiguration',
            options={'ordering': ['last_data_import'], 'verbose_name': 'Import configuration', 'verbose_name_plural': 'Import configurations'},
        ),
        migrations.AlterField(
            model_name='dataimportconfiguration',
            name='github_url_for_import_data',
            field=models.URLField(blank=True, default='https://raw.githubusercontent.com/pcm-dpc/COVID-19/refs/heads/master/dati-json/dpc-covid19-ita-province.json', null=True, verbose_name='Github URL for import data'),
        ),
    ]
