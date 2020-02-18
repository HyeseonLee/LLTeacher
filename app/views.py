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
    model = GeneralChemistry2
    
    def get(self, request, *arg, **kwargs):
        template_name = 'GeneralChemistry2.html'
        gc2 = GeneralChemistry2.objects.all()
        return render(request, template_name, {'gc2':gc2})
<<<<<<< HEAD
=======

class LERead(ListView):
    model = LawAndEconomics
    
    def get(self, request, *arg, **kwargs):
        template_name = 'LE.html'
        LE = GeneralChemistry2.objects.all()
        return render(request, template_name, {'LE':LE})

class PERead(ListView):
    model = PhysicsExperiment
    
    def get(self, request, *arg, **kwargs):
        template_name = 'PE.html'
        PE = PhysicsExperiment.objects.all()
        return render(request, template_name, {'PE':PE})    

class WPRead(ListView):
    model = WebProgramming
    
    def get(self, request, *arg, **kwargs):
        template_name = 'WP.html'
        WP = WebProgramming.objects.all()
        return render(request, template_name, {'WP':WP})
    
    
>>>>>>> 59dffcd4d0530f30d2a48c7381f75d5843c9a6fc
    
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
    
