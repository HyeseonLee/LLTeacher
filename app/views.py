from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # 근데 이거 사용법 까먹었어요...  // redirect 와 유사한거같아!

from .models import GeneralChemistry2, LawAndEconomics, PhysicsExperiment, WebProgramming

modelList = [GeneralChemistry2, LawAndEconomics, PhysicsExperiment, WebProgramming]
professorNameGC = "최슬옹"

def index(request):
    contentsGC = GeneralChemistry2.objects.all()
    countGC = 0
    sumGC = 0
    avgGC = "등록해줘~"
    for content in contentsGC:    
        sumGC += content.score
        countGC +=1
        avgGC = round(sumGC/countGC, 2)
    latestGC = GeneralChemistry2.objects.order_by('-pk').first()

    contentsLE = LawAndEconomics.objects.all()
    countLE = 0
    sumLE = 0
    avgLE = "등록해줘~"
    for content in contentsLE:    
        sumLE += content.score
        countLE +=1
        avgLE = round(sumLE/countLE, 2)
    latestLE = LawAndEconomics.objects.order_by('-pk').first()

    contentsPE = PhysicsExperiment.objects.all()
    countPE = 0
    sumPE = 0
    avgPE = "등록해줘~"
    for content in contentsPE:    
        sumPE += content.score
        countPE +=1
        avgPE = round(sumPE/countPE, 2)
    latestPE = PhysicsExperiment.objects.order_by('-pk').first()

    contentsWP = WebProgramming.objects.all()
    countWP = 0
    sumWP = 0
    avgWP = "등록해줘~"
    for content in contentsWP:    
        sumWP += content.score
        countWP +=1
        avgWP = round(sumWP/countWP, 2)
    latestWP = WebProgramming.objects.order_by('-pk').first()

    return render(request, 'index.html', { 'professorNameGC':professorNameGC, 'avgGC' : avgGC , 'avgLE' : avgLE, 'avgPE':avgPE, 'avgWP':avgWP , 'latestGC':latestGC, 'latestLE':latestLE, 'latestPE':latestPE, 'latestWP':latestWP})

class GC2Read(ListView):
    model = GeneralChemistry2
    def get(self, request): 
        template_name = 'GC2.html' 
        GC2 = GeneralChemistry2.objects.all().order_by('-time')
        return render(request, template_name, {'GC2':GC2})

class LERead(ListView):
    model = LawAndEconomics
    def get(self, request):
        template_name = 'LE.html'
        LE = LawAndEconomics.objects.all().order_by('-time')
        return render(request, template_name, {'LE':LE})

class PERead(ListView):
    model = PhysicsExperiment
    
    def get(self, request):
        template_name = 'PE.html'
        PE = PhysicsExperiment.objects.all().order_by('-time')
        return render(request, template_name, {'PE':PE})    

class WPRead(ListView):
    model = WebProgramming
    
    def get(self, request):
        template_name = 'WP.html'
        WP = WebProgramming.objects.all().order_by('-time')
        return render(request, template_name, {'WP':WP})
 
#CREATEVIEW

class GC2Create(CreateView):
    model = GeneralChemistry2
    template_name = 'gc2_create_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('GC2')

class LECreate(CreateView):
    model = LawAndEconomics
    template_name = 'le_create_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('LE')

class PECreate(CreateView):
    model = PhysicsExperiment
    template_name = 'pe_create_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('PE')

class WPCreate(CreateView):
    model = WebProgramming
    template_name = 'wp_create_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('WP')
    
#UPDATEVIEW

class GC2Update(UpdateView):
    model = GeneralChemistry2
    template_name = 'gc2_update_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('GC2')

class LEUpdate(UpdateView):
    model = LawAndEconomics
    template_name = 'le_update_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('LE')

class PEUpdate(UpdateView):
    model = PhysicsExperiment
    template_name = 'pe_update_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('PE')

class WPUpdate(UpdateView):
    model = WebProgramming
    template_name = 'wp_update_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('WP')
 
#DELETEVIEW    

class GC2Delete(DeleteView):
    model = GeneralChemistry2
    template_name = 'gc2_delete_form.html'
    success_url = reverse_lazy('GC2')

class LEDelete(DeleteView):
    model = GeneralChemistry2
    template_name = 'le_delete_form.html'
    success_url = reverse_lazy('LE')

class PEDelete(DeleteView):
    model = GeneralChemistry2
    template_name = 'pe_delete_form.html'
    success_url = reverse_lazy('PE')

class WPDelete(DeleteView):
    model = GeneralChemistry2
    template_name = 'wp_delete_form.html'
    success_url = reverse_lazy('WP')
   
# 로그인 관련코드.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username= request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('main')
    return render(request, 'user_signup.html')

def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username , password = password)
            
            if user is not None:
                auth.login(request,user)
                return redirect('main')    
            else:
                errormasg = "잘못입력하셨습니다"
                return render(request, 'user_login.html',{'errormasg':errormasg})
        else:
            return redirect('user_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def loginhome(request):
    return render(request,'user_login.html')

def signuphome(request):
    return render(request, 'user_signup.html')

def mypage(request):
    render_args = {}
    for model in modelList:
        post = model.objects.filter(author = request.user)
        render_args['posts'] = post
    return render(request, 'mypage.html', render_args)