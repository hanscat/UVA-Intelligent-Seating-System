from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at Dr. Fourier's project index.")
    return render(request, 'index.html')

def test(request):
    return render(request, 'index.html')