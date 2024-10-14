from django.db import models


# Create your models here.
class DataImportProvince(models.Model):
    data = models.DateTimeField("Data", blank=True, null=True)
    stato = models.CharField("Stato", blank=True, null=True, max_length=255)
    codice_regione = models.IntegerField("Codice regione", blank=True, null=True)
    denominazione_regione = models.CharField("Denominazione regione", blank=True, null=True, max_length=255)
    codice_provincia = models.IntegerField("Codice provincia", blank=True, null=True)
    denominazione_provincia = models.CharField("Denominazione provincia", blank=True, null=True, max_length=255)
    sigla_provincia = models.CharField("Sigla provincia", blank=True, null=True, max_length=255)
    lat = models.FloatField("Latitude", blank=True, null=True)
    long = models.FloatField("Longitude", blank=True, null=True)
    totale_casi = models.IntegerField("Totale casi", blank=True, null=True)
    note = models.TextField("Note", blank=True, null=True)
    codice_nuts_1 = models.CharField("Codice nuts 1", blank=True, null=True, max_length=255)
    codice_nuts_2 = models.CharField("Codice nuts 2", blank=True, null=True, max_length=255)
    codice_nuts_3 = models.CharField("Codice nuts 3", blank=True, null=True, max_length=255)

    def __str__(self):
        return "{}, codice {} - {}, codice {}".format(self.denominazione_provincia,
                                                      self.codice_provincia,
                                                      self.denominazione_regione,
                                                      self.denominazione_provincia)

    class Meta:
        verbose_name = "Dato provincia importato da GitHub"
        verbose_name_plural = "Dati provincia importati da GitHub"
        ordering = ('codice_provincia', 'denominazione_provincia')
