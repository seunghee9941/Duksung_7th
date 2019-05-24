from django.shortcuts import render, get_object_or_404, redirect
from .forms import ApplyForm
from .models import Apply
from django.http import HttpResponse

# Create your views here.

# 지원하기
def form(request):
    if request.method == "POST":
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            board = form.save(commit = False)
            board.save()
            return HttpResponse('apply/form')
    else:
        form = ApplyForm()
        return render(request, 'form.html', {'form':form})


def adview(request):
    applies = Apply.objects.all()
    return render(request, 'adview.html', {'applies' : applies})
