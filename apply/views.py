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
        print("a")
        print(form)
        
        if request.POST.get('_save')=="임시저장": # 지원서 임시저장
                print("b")
                if request.method == "POST":
                        print("c")
                        if form.is_valid():
                                board = form.save(commit = True)
                                print(board)
                                print(board.name)
                                board.isFinal=False
                                print(board.isFinal)
                                board.save()
                                return HttpResponseRedirect('save')
                else:
                        form = ApplyForm()
                        return render(request, 'form.html', {'form':form})
        print("d")
        if request.POST.get('_submit')=="제출": # 지원서 제출
                print("e")
                if request.method == "POST":
                        print("f")
                        if form.is_valid():
                                board = form.save(commit = True)
                                board.isFinal=True
                                print(board)
                                print(board.name)
                                print(board.isFinal)
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