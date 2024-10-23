from datetime import timezone, datetime

from django.db import models


# Create your models here.
class DataImportProvince(models.Model):
    data = models.DateTimeField("Data", blank=True, null=True)
    state = models.CharField("State", blank=True, null=True, max_length=255)
    region_code = models.IntegerField("Region code", blank=True, null=True)
    region_name = models.CharField("Region name", blank=True, null=True, max_length=255)
    province_code = models.IntegerField("Province code", blank=True, null=True)
    province_name = models.CharField("Province name", blank=True, null=True, max_length=255)
    province_abbreviation = models.CharField("Province abbreviation", blank=True, null=True, max_length=255)
    lat = models.FloatField("Latitude", blank=True, null=True)
    long = models.FloatField("Longitude", blank=True, null=True)
    total_cases = models.IntegerField("Total of cases", blank=True, null=True)
    note = models.TextField("Note", blank=True, null=True)
    codice_nuts_1 = models.CharField("Nuts code 1", blank=True, null=True, max_length=255)
    codice_nuts_2 = models.CharField("Nuts code 2", blank=True, null=True, max_length=255)
    codice_nuts_3 = models.CharField("Nuts code 3", blank=True, null=True, max_length=255)

    def __str__(self):
        return "{}, codice {} - {}, codice {}".format(self.province_name,
                                                      self.province_code,
                                                      self.region_name,
                                                      self.region_code)

    class Meta:
        verbose_name = "Province data imported from GitHub"
        verbose_name_plural = "Province data imported from GitHub"
        ordering = ('province_code', 'province_name')


class DataImportConfiguration(models.Model):
    last_data_import = models.DateTimeField("Data", blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    github_url_for_import_data = models.URLField(
        "Github URL for import data", blank=True, null=True,
        default="https://raw.githubusercontent.com/pcm-dpc/COVID-19/refs/heads/master/dati-json/dpc-covid19-ita-province-latest.json")

    def __str__(self):
        return "{}".format(self.last_data_import)

    @staticmethod
    def get_config():
        try:
            data_import_config = DataImportConfiguration.objects.all()[0]
        except:
            data_import_config = DataImportConfiguration(last_data_import=datetime.today())
            data_import_config.save()

        return data_import_config

    def update_last_data_import(self):
        self.last_data_import = datetime.today()
        self.save()

    class Meta:
        verbose_name = "Import configuration"
        verbose_name_plural = "Import configurations"
        ordering = ['last_data_import']
