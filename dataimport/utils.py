from dataimport.models import DataImportProvince


def process_import_data(import_data):
    objects_to_create = []
    for row in import_data:
        obj = DataImportProvince(
            region_code=row['codice_regione'],
            province_code=row['codice_provincia'],
            data=row['data'],
            state=row['stato'],
            region_name=row['denominazione_regione'],
            province_name=row['denominazione_provincia'],
            province_abbreviation=row['sigla_provincia'],
            lat=row['lat'],
            long=row['long'],
            total_cases=row['totale_casi'],
            note=row['note'],
            codice_nuts_1=row['codice_nuts_1'],
            codice_nuts_2=row['codice_nuts_2'],
            codice_nuts_3=row['codice_nuts_3']
        )
        objects_to_create.append(obj)

    DataImportProvince.objects.bulk_create(objects_to_create, batch_size=1000)
