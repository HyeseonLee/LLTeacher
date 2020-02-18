from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # 근데 이거 사용법 까먹었어요...

from .models import GeneralChemistry2, LawAndEconomics, PhysicsExperiment, WebProgramming

def index(request):
    contentsGC = GeneralChemistry2.objects.all()
    countGC = 0
    sumGC = 0
    for content in contents:    
        sumGC += content.score
        countGC +=1
    avgGC = sumGC/count

    return render(request, 'index.html', { 'sumGC' : sumGC })
    

class GC2Read(ListView):
    model = GeneralChemistry2
    
    def get(self, request, *arg, **kwargs):
        template_name = 'GeneralChemistry2.html'
        gc2 = GeneralChemistry2.objects.all()
        return render(request, template_name, {'gc2':gc2})
    
    
    
class GC2Create(CreateView):
    model = GeneralChemistry2
    fields = ['seme','score','text']
    success_url = reverse_lazy('GC2')
    # GC2 는 URLS.PY 속 NAME인 것 같습니다요
    # 성공하면 어디로 이동할까요~?

class GC2Update(UpdateView):
    model = GeneralChemistry2
    fields = ['seme','score','text']
    template_name_suffix = 'GC2_update_form'

class GC2Delete(DeleteView):
    model = GeneralChemistry2
    success_url = reverse_lazy('GC2')
    
