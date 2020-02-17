from django.shortcuts import render
from django.views.generic import ListView

from .models import GeneralChemistry2

# Create your views here.
class GC2LV(ListView):
    model = GeneralChemistry2
    template_name = 'GeneralChemistry2.html'

