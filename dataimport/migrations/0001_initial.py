# Generated by Django 4.1.2 on 2024-10-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataImportProvince',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(blank=True, null=True, verbose_name='Data')),
                ('stato', models.CharField(blank=True, max_length=255, null=True, verbose_name='Stato')),
                ('codice_regione', models.IntegerField(blank=True, null=True, verbose_name='Codice regione')),
                ('denominazione_regione', models.CharField(blank=True, max_length=255, null=True, verbose_name='Denominazione regione')),
                ('codice_provincia', models.IntegerField(blank=True, null=True, verbose_name='Codice provincia')),
                ('denominazione_provincia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Denominazione provincia')),
                ('sigla_provincia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sigla provincia')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('long', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('totale_casi', models.IntegerField(blank=True, null=True, verbose_name='Totale casi')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('codice_nuts_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Codice nuts 1')),
                ('codice_nuts_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Codice nuts 2')),
                ('codice_nuts_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Codice nuts 3')),
            ],
            options={
                'verbose_name': 'Dato provincia importato da GitHub',
                'verbose_name_plural': 'Dati provincia importati da GitHub',
                'ordering': ('codice_provincia', 'denominazione_provincia'),
            },
        ),
    ]