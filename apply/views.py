from django.shortcuts import render, get_object_or_404, redirect
from .models import Apply
from .forms import ApplyForm
from .models import Apply
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def addetail(request,apply_id):
    #applys = apply.objects #쿼리셋 #메소드
    apply_addeatil = get_object_or_404(Apply, pk = apply_id)
    return render(request,'addetail.html',{'applys': apply_addeatil})

# 지원하기
def form(request):
        # action = request.POST.get('submit')
        form = ApplyForm(request.POST, request.FILES)
        if request.POST.get('_save')=="임시저장": # 지원서 임시저장
                if request.method == "POST":
                        if form.is_valid():
                                board = form.save(commit = True)
                                board.isFinal=False
                                board.save()
                                return HttpResponseRedirect('save')
                else:
                        form = ApplyForm()
                        return render(request, 'form.html', {'form':form})
        if request.POST.get('_submit')=="제출": # 지원서 제출
                if request.method == "POST":
                        if form.is_valid():
                                board = form.save(commit = True)
                                board.isFinal=True
                                board.save()
                                return HttpResponseRedirect('submit')
                else:
                        form = ApplyForm()
                        return render(request, 'form.html', {'form':form})
        return render(request, 'form.html', {'form':form})

def adview(request):
    applies = Apply.objects.all()
    return render(request, 'adview.html', {'applies' : applies})

def save(request):
        return render(request, 'save.html')

def submit(request):
        return render(request, 'submit.html')