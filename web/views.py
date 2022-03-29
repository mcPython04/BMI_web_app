from django.http import HttpResponse
from django.shortcuts import render
from . import calculation


# Create your views here.
def home(request):
    return render(request, 'web/home.html')


def result(request):
    if request.method == 'POST':
        feet = request.POST["feet"]
        inch = request.POST["inches"]
        weight = request.POST["weight"]

        bmi = round(calculation.calculate_bmi(int(feet), int(inch), int(weight)), 2)

        context = {
            'feet': feet,
            'inch': inch,
            'weight': weight,
            'bmi': bmi
        }
        return render(request, 'web/result.html', context)

