from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'web/home.html')


def result(request):
    if request.method == 'POST':
        feet = request.POST["feet"]
        inch = request.POST["inches"]

