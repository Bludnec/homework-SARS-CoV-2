from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def province_table(request):
    return render(request, 'province_table.html', {"ciao": "ciao"})
