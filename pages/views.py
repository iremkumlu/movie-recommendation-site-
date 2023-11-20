from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# render metodu


def index(request):
    return render(request, 'pages/index.html')


def contact(request):
    return render(request, 'pages/contact.html')  # film detayi sayfasi


def about(request):
    return render(request, 'pages/about.html')  # film detayi sayfasi

