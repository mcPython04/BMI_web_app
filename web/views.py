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

        bmi = round(calculation.calculate_bmi(int(feet), int(inch), int(weight)), 1)
        flag = ""

        if bmi < 18.5:
            flag = "Underweight"

        elif bmi >= 18.5 and bmi < 25:
            flag = "Normal Weight"

        elif bmi >= 25.0 and bmi < 30:
            flag = "Overweight"

        elif bmi >= 30:
            flag = "Obese"

        context = {
            'feet': feet,
            'inch': inch,
            'weight': weight,
            'bmi': bmi,
            'flag': flag
        }
        return render(request, 'web/result.html', context)

