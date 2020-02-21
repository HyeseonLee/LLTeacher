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
        template_name = 'GeneralChemistry2.html'   
        # 'GeneralChemistry2.html' 라는 HTML파일로 작업할꺼야 근데 CreateView UpdateView DeleteView 를 
        # 각각 html 안만들고 하나의 html 속 각각의 form으로 동작하고싶은데
        GC2 = GeneralChemistry2.objects.all().order_by('-time')
        # -time 기준으로 정렬 ==> 최신 후기를 상단에 출력해줌
        return render(request, template_name, {'GC2':GC2 , "professorNameGC" : professorNameGC})

class LERead(ListView):
    model = LawAndEconomics
    # html 에 object_list 속에 객체가 담기는데 조작은 어떻게하지? for i in object_list
    # context_object_name = '' 을 이용해 수정
    # pk 를 이용하느건 object 로만
    def get(self, request):
        template_name = 'LE.html'
        LE = GeneralChemistry2.objects.all().order_by('-time')
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
    
class GC2Create(CreateView):
    model = GeneralChemistry2
    template_name = 'generalchemistry2_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('GC2_CREATE')
    

class GC2Update(UpdateView):
    model = GeneralChemistry2
    template_name = 'generalchemistry2_update_form.html'
    fields = ['seme','score','text']
    success_url = reverse_lazy('GC2')
    
    #(소문자모델)_form.html

class GC2Delete(DeleteView):
    model = GeneralChemistry2
    template_name = 'gc2_confirm_delete.html'
    success_url = reverse_lazy('GC2')
    #(소문자모델)_confirm_delete.html
    

    # 아래는 로그인 관련코드.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username= request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('main')
    return render(request, 'login.html')

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
                return render(request, 'login.html',{'errormasg':errormasg})
        else:
            return redirect('login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


# def delete(request, account_id):
#         account = Account.objects.get(id=account_id)
#         account.delete()
#         return redirect('index')

def loginhome(request):
    return render(request,'login.html')

def mypage(request):
    return render(request, 'mypage.html')
