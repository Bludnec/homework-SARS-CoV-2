from django.shortcuts import render


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
        'page_title': 'Tabella dati per provincia'
    }
    return render(request, 'province_table.html', data_dict)
