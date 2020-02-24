from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect

from .models import GeneralChemistry2, LawAndEconomics, PhysicsExperiment, WebProgramming

modelList = [GeneralChemistry2, LawAndEconomics, PhysicsExperiment, WebProgramming]

def index(request):
    contentsGC = GeneralChemistry2.objects.all()
    countGC = 0
    sumGC = 0
    avgGC = "등록해줘~"
    professorNameGC="초기이름"
    for content in contentsGC:    
        sumGC += content.score
        countGC +=1
        avgGC = round(sumGC/countGC, 2)
        professorNameGC = content.professorName
    latestGC = GeneralChemistry2.objects.order_by('-pk').first()

    contentsLE = LawAndEconomics.objects.all()
    countLE = 0
    sumLE = 0
    avgLE = "등록해줘~"
    professorNameLE="초기이름"
    for content in contentsLE:    
        sumLE += content.score
        countLE +=1
        avgLE = round(sumLE/countLE, 2)
        professorNameLE = content.professorName
    latestLE = LawAndEconomics.objects.order_by('-pk').first()

    contentsPE = PhysicsExperiment.objects.all()
    countPE = 0
    sumPE = 0
    avgPE = "등록해줘~"
    professorNamePE="초기이름"
    for content in contentsPE:    
        sumPE += content.score
        countPE +=1
        avgPE = round(sumPE/countPE, 2)
        professorNamePE = content.professorName
    latestPE = PhysicsExperiment.objects.order_by('-pk').first()

    contentsWP = WebProgramming.objects.all()
    countWP = 0
    sumWP = 0
    avgWP = "등록해줘~"
    professorNameWP="초기이름"
    for content in contentsWP:    
        sumWP += content.score
        countWP +=1
        avgWP = round(sumWP/countWP, 2)
        professorNameWP = content.professorName
    latestWP = WebProgramming.objects.order_by('-pk').first()

    return render(request, 'index.html', { 'professorNameGC':professorNameGC, 'professorNameLE':professorNameLE, 'professorNamePE':professorNamePE,'professorNameWP':professorNameWP,'avgGC' : avgGC , 'avgLE' : avgLE, 'avgPE':avgPE, 'avgWP':avgWP , 'latestGC':latestGC, 'latestLE':latestLE, 'latestPE':latestPE, 'latestWP':latestWP})

class GC2Read(ListView):
    model = GeneralChemistry2

    def get(self, request): 
        template_name = 'GC2.html' 
        GC2 = GeneralChemistry2.objects.all().order_by('-time')
        contentsGC = GeneralChemistry2.objects.all()
        countGC = 0
        sumGC = 0
        avgGC = "등록해줘~"
        for content in contentsGC:    
            sumGC += content.score
            countGC +=1
            avgGC = round(sumGC/countGC, 2)
        return render(request, template_name, {'GC2':GC2,'avgGC':avgGC})

class LERead(ListView):
    model = LawAndEconomics
    def get(self, request):
        template_name = 'LE.html'
        LE = LawAndEconomics.objects.all().order_by('-time')
        contentsLE = LawAndEconomics.objects.all()
        countLE = 0
        sumLE = 0
        avgLE = "등록해줘~"
    
        for content in contentsLE:    
            sumLE += content.score
            countLE +=1
            avgLE = round(sumLE/countLE, 2)
        return render(request, template_name, {'LE':LE,'avgLE':avgLE})

class PERead(ListView):
    model = PhysicsExperiment
    
    def get(self, request):
        template_name = 'PE.html'
        PE = PhysicsExperiment.objects.all().order_by('-time')
        contentsPE = PhysicsExperiment.objects.all()
        countPE = 0
        sumPE = 0
        avgPE = "등록해줘~"

        for content in contentsPE:    
            sumPE += content.score
            countPE +=1
            avgPE = round(sumPE/countPE, 2)
        return render(request, template_name, {'PE':PE,'avgPE':avgPE})    

class WPRead(ListView):
    model = WebProgramming
    
    def get(self, request):
        template_name = 'WP.html'
        WP = WebProgramming.objects.all().order_by('-time')
        contentsWP = WebProgramming.objects.all()
        countWP = 0
        sumWP = 0
        avgWP = "등록해줘~"

        for content in contentsWP:    
            sumWP += content.score
            countWP +=1
            avgWP = round(sumWP/countWP, 2)
        return render(request, template_name, {'WP':WP,'avgWP':avgWP})
 
#CREATEVIEW

class GC2Create(CreateView):
    model = GeneralChemistry2
    template_name = 'gc2_create_form.html'
    fields = ['seme','score','text']
    
    def form_valid(self,form):
        GeneralChemistry2 = form.save(commit=False)
        GeneralChemistry2.author = self.request.user
        GeneralChemistry2.save()

        return HttpResponseRedirect(self.request.POST.get('next', '/'))

class LECreate(CreateView):
    model = LawAndEconomics
    template_name = 'gc2_create_form.html'
    fields = ['seme','score','text']
    
    def form_valid(self,form):
        LawAndEconomics = form.save(commit=False)
        LawAndEconomics.author = self.request.user
        LawAndEconomics.save()

        return HttpResponseRedirect(self.request.POST.get('next', '/'))

class PECreate(CreateView):
    model = PhysicsExperiment
    template_name = 'gc2_create_form.html'
    fields = ['seme','score','text']
    
    def form_valid(self,form):
        PhysicsExperiment = form.save(commit=False)
        PhysicsExperiment.author = self.request.user
        PhysicsExperiment.save()

        return HttpResponseRedirect(self.request.POST.get('next', '/'))

class WPCreate(CreateView):
    model = WebProgramming
    template_name = 'gc2_create_form.html'
    fields = ['seme','score','text']
    
    def form_valid(self,form):
        WebProgramming = form.save(commit=False)
        WebProgramming.author = self.request.user
        WebProgramming.save()

        return HttpResponseRedirect(self.request.POST.get('next', '/'))
    
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
    model = LawAndEconomics
    template_name = 'le_delete_form.html'
    success_url = reverse_lazy('LE')

class PEDelete(DeleteView):
    model = PhysicsExperiment
    template_name = 'pe_delete_form.html'
    success_url = reverse_lazy('PE')

class WPDelete(DeleteView):
    model = WebProgramming
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

# def logout(request):
#     auth.logout(request)
#     return render(request, 'index.html')
# 로그아웃 함수 추가
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'index.html')


def loginhome(request):
    return render(request,'user_login.html')

def signuphome(request):
    return render(request, 'user_signup.html')

def mypage(request):
    GC2 = GeneralChemistry2.objects.filter(author=request.user).order_by('-time')
    PE = PhysicsExperiment.objects.filter(author=request.user).order_by('-time')
    WP = WebProgramming.objects.filter(author=request.user).order_by('-time')
    LE = LawAndEconomics.objects.filter(author=request.user).order_by('-time')

    countGC=0
    countPE=0
    countWP=0
    countLE=0
    countall=0

    for content in GC2:
        countGC += 1
    for content in PE:
        countPE += 1
    for content in WP:
        countWP += 1
    for content in LE:
        countLE += 1
    countall = countGC+countPE+countWP+countLE

    return render(request, 'mypage.html', {'GC2':GC2, 'PE':PE, 'WP':WP, 'LE':LE,'countall':countall, 'countGC':countGC, 'countPE':countPE, 'countWP':countWP, 'countLE':countLE})

#검색창 코드
def result(request):
    GC2posts = GeneralChemistry2.objects.all()
    PEposts = PhysicsExperiment.objects.all()
    WPposts = WebProgramming.objects.all()
    LEposts = LawAndEconomics.objects.all()

    countGC=0
    countPE=0
    countWP=0
    countLE=0
    countall=0

    query = request.GET.get('query','')

    if query:
        GC2posts = GC2posts.filter(Q(lectureName__icontains=query)| Q(professorName__icontains=query)).order_by('-time')
        PEposts  = PEposts.filter(Q(lectureName__icontains=query)| Q(professorName__icontains=query)).order_by('-time')
        WPposts  = WPposts.filter(Q(lectureName__icontains=query)| Q(professorName__icontains=query)).order_by('-time')
        LEposts  = LEposts.filter(Q(lectureName__icontains=query)| Q(professorName__icontains=query)).order_by('-time')

        for content in GC2posts:
            countGC += 1
        for content in PEposts:
            countPE += 1
        for content in WPposts:
            countWP += 1
        for content in LEposts:
            countLE += 1
        countall = countGC+countPE+countWP+countLE
    return render(request, 'result.html',{'GC2posts':GC2posts, 'PEposts':PEposts, 'WPposts':WPposts, 'LEposts':LEposts,'query':query,'countall':countall})
