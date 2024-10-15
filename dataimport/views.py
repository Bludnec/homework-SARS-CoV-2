import json

import requests
from django.db.models import Sum, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from dataimport.utils import *


# Create your views here.
def home(request):
    data_dict = {
        'page': 'home',
        'page_title': 'Home'
    }
    return render(request, 'home.html', data_dict)


def province_table(request):
    data_dict = {
        'page': 'province-table',
        'page_title': 'Province data table'
    }
    return render(request, 'province_table.html', data_dict)


@csrf_exempt
def data_import_province_table_ajax(request):
    draw = int(request.POST.get("draw", 1))
    start = int(request.POST.get("start", 0))
    length = int(request.POST.get("length", 0))

    order_column = int(request.POST.get("order[0][column]", 2))
    order_dir = request.POST.get("order[0][dir]", "desc")
    order_column_name = request.POST.get("columns[%s][data]" % order_column, "total_cases_sum")

    if order_column_name == 'total_cases':
        order_column_name = 'total_cases_sum'

    if order_dir == "desc":
        order_string = "-%s" % order_column_name
    else:
        order_string = "%s" % order_column_name

    if order_column_name == 'total_cases_sum':
        queryset = (
            DataImportProvince.objects
            .values('region_code', 'region_name')
            .annotate(
                total_cases_sum=Sum('total_cases'),
                numero_province=Count('id')
            )
        ).order_by(order_string, 'region_name')
    else:
        queryset = (
            DataImportProvince.objects
            .values('region_code', 'region_name')
            .annotate(
                total_cases_sum=Sum('total_cases'),
                numero_province=Count('id')
            )
        ).order_by(order_string)

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
    url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/refs/heads/master/dati-json/dpc-covid19-ita-province-latest.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Controlla se la richiesta ha avuto successo
        data = response.json()  # Parsea il JSON
        process_import_data(data)
        return JsonResponse({'result': "OK"}, status=200)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
