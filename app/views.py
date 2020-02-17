from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
# 근데 이거 사용법 까먹었어요...

from .models import GeneralChemistry2

# Create your views here.
class GC2Read(ListView):
    model = GeneralChemistry2
    template_name = 'GeneralChemistry2.html'

# class GC2Create(CreateView):
#     model = GeneralChemistry2
#     fields = ['seme','score','text']
#     # success_url = reverse_lazy('GeneralChemistry2')????

# class GC2Update(UpdateView):

# class GC2Delete(DeleteView):
