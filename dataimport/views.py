import json
from datetime import datetime

import requests
from django.db.models import Sum, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from dataimport.models import DataImportConfiguration
from dataimport.utils import *


# Create your views here.
def home(request):
    data_dict = {
        'page': 'home',
        'page_title': 'Small documentation'
    }
    return render(request, 'home.html', data_dict)


def province_table(request):
    data_import_config = DataImportConfiguration.get_config()
    last_data_import = data_import_config.last_data_import.strftime("%H:%M, %d %B %Y")
    data_exists = DataImportProvince.objects.exists()
    data_dict = {
        'page': 'province-table',
        'page_title': 'Province data table',
        'last_data_import': last_data_import,
        'data_exists': data_exists
    }
    return render(request, 'province_table.html', data_dict)


@csrf_exempt
def data_import_province_table_ajax(request):
    data_import_config = DataImportConfiguration.get_config()
    if not data_import_config.last_data_import.date() == datetime.today().date() or not DataImportProvince.objects.exists():
        data_import_province_from_github(request)

    draw = int(request.POST.get("draw", 1))
    start = int(request.POST.get("start", 0))
    length = int(request.POST.get("length", 0))

    order_column = int(request.POST.get("order[0][column]", 2))
    order_dir = request.POST.get("order[0][dir]", "desc")
    order_column_name = request.POST.get("columns[%s][data]" % order_column, "total_cases_sum")

    date_range_from = request.POST.get("date_range_from", None)
    date_range_to = request.POST.get("date_range_to", None)



    if order_column_name == 'total_cases':
        order_column_name = 'total_cases_sum'

    if order_dir == "desc":
        order_string = "-%s" % order_column_name
    else:
        order_string = "%s" % order_column_name

    queryset = DataImportProvince.objects.all()

    if date_range_from:
        date_range_from_datetime = datetime.strptime(date_range_from, '%d/%m/%Y')
        queryset = queryset.filter(data__gte=date_range_from_datetime)
    if date_range_to:
        date_range_to_datetime = datetime.strptime(date_range_to, '%d/%m/%Y')
        queryset = queryset.filter(data__lte=date_range_to_datetime)

    queryset = (
        queryset.values('region_code', 'region_name')
        .annotate(
            total_cases_sum=Sum('total_cases'),
            numero_province=Count('id')
        ))

    if order_column_name == 'total_cases_sum':
        queryset = queryset.order_by(order_string, 'region_name')
    else:
        queryset = queryset.order_by(order_string)

    count = queryset.count()

    response = {
        "draw": draw,
        "recordsTotal": count,
        "recordsFiltered": count,
        "data": []
    }
    for el in queryset[start:length + start]:
        response['data'].append({
            "region_code": el['region_code'],
            "region_name": el['region_name'],
            "total_cases": el['total_cases_sum'],
            "numero_province": el['numero_province'],
        })
    return HttpResponse(json.dumps(response), content_type="application/json")


def data_import_province_from_github(request):
    data_import_configuration = DataImportConfiguration.get_config()
    try:
        url = data_import_configuration.github_url_for_import_data
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Delete all the data to avoid conflicts or missing data
        DataImportProvince.objects.all().delete()
        # Import the new data
        process_import_data(data)

        # Update last data import
        data_import_configuration.update_last_data_import()

        return JsonResponse({'result': "OK"}, status=200)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
