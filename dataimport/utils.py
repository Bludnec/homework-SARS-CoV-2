from dataimport.models import DataImportProvince


def process_import_data(import_data):
    for row in import_data:
        DataImportProvince.objects.update_or_create(
            # Campi di riferimento per cercare l'oggetto esistente
            region_code=row['codice_regione'],
            province_code=row['codice_provincia'],
            # Valori da aggiornare o impostare se l'oggetto non esiste
            defaults={
                'data': row['data'],
                'state': row['stato'],
                'region_name': row['denominazione_regione'],
                'province_name': row['denominazione_provincia'],
                'province_abbreviation': row['sigla_provincia'],
                'lat': row['lat'],
                'long': row['long'],
                'total_cases': row['totale_casi'],
                'note': row['note'],
                'codice_nuts_1': row['codice_nuts_1'],
                'codice_nuts_2': row['codice_nuts_2'],
                'codice_nuts_3': row['codice_nuts_3'],
            }
        )
