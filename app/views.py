from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # 근데 이거 사용법 까먹었어요...

from .models import GeneralChemistry2, LawAndEconomics, PhysicsExperiment, WebProgramming

def index(request):
    contentsGC = GeneralChemistry2.objects.all()
    countGC = 0
    sumGC = 0
    for content in contentsGC:    
        sumGC += content.score
        countGC +=1
    avgGC = sumGC/countGC
    latestGC = GeneralChemistry2.objects.order_by('-pk').first()

    contentsLE = LawAndEconomics.objects.all()
    countLE = 0
    sumLE = 0
    for content in contentsLE:    
        sumLE += content.score
        countLE +=1
    avgLE = sumLE/countLE
    latestLE = LawAndEconomics.objects.order_by('-pk').first()

    contentsPE = PhysicsExperiment.objects.all()
    countPE = 0
    sumPE = 0
    for content in contentsPE:    
        sumPE += content.score
        countPE +=1
    avgPE = sumPE/countPE
    latestPE = PhysicsExperiment.objects.order_by('-pk').first()

    contentsWP = WebProgramming.objects.all()
    countWP = 0
    sumWP = 0
    for content in contentsWP:    
        sumWP += content.score
        countWP +=1
    avgWP = sumWP/countWP
    latestWP = WebProgramming.objects.order_by('-pk').first()

    return render(request, 'index.html', { 'avgGC' : avgGC , 'avgLE' : avgLE, 'avgPE':avgPE, 'avgWP':avgWP , 'latestGC':latestGC, 'latestLE':latestLE, 'latestPE':latestPE, 'latestWP':latestWP})

class GC2Read(ListView):
    def get(self, request, *arg, **kwargs):
        model = GeneralChemistry2
        template_name = 'GeneralChemistry2.html'
        latestGC = model.objects.order_by('-pk').first()
        gc2 = model.objects.all()
        return render(request, template_name, {'gc2':gc2, 'latestGC':latestGC})
        
class LERead(ListView):
    def get(self, request, *arg, **kwargs):
        model = LawAndEconomics
        template_name = 'LE.html'
        LE = model.objects.all()
        latestLE = model.objects.order_by('-pk').first()
        return render(request, template_name, {'LE':LE, 'latestLE':latestLE})

class PERead(ListView):
    def get(self, request, *arg, **kwargs):
        model = PhysicsExperiment
        template_name = 'PE.html'
        PE = model.objects.all()
        latestPE = model.objects.order_by('-pk').first()
        return render(request, template_name, {'PE':PE, 'latestPE':latestPE})    

class WPRead(ListView):
    def get(self, request, *arg, **kwargs):
        model = WebProgramming
        template_name = 'WP.html'
        WP = model.objects.all()
        latestWP = model.objects.order_by('-pk').first()
        return render(request, template_name, {'WP':WP, 'latestWP':latestWP})
    
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
    
