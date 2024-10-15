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
