from dataimport.models import DataImportProvince


def process_import_data(import_data):
    for row in import_data:
        DataImportProvince.objects.update_or_create(
            # Campi di riferimento per cercare l'oggetto esistente
            codice_regione=row['codice_regione'],
            codice_provincia=row['codice_provincia'],
            # Valori da aggiornare o impostare se l'oggetto non esiste
            defaults={
                'data': row['data'],
                'stato': row['stato'],
                'denominazione_regione': row['denominazione_regione'],
                'denominazione_provincia': row['denominazione_provincia'],
                'sigla_provincia': row['sigla_provincia'],
                'lat': row['lat'],
                'long': row['long'],
                'totale_casi': row['totale_casi'],
                'note': row['note'],
                'codice_nuts_1': row['codice_nuts_1'],
                'codice_nuts_2': row['codice_nuts_2'],
                'codice_nuts_3': row['codice_nuts_3'],
            }
        )
