# Generated by Django 5.1rc1 on 2024-10-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataimport', '0006_alter_dataimportconfiguration_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataimportconfiguration',
            name='github_url_for_import_data',
            field=models.URLField(blank=True, default='https://raw.githubusercontent.com/pcm-dpc/COVID-19/refs/heads/master/dati-json/dpc-covid19-ita-province-latest.json', null=True, verbose_name='Github URL for import data'),
        ),
    ]
