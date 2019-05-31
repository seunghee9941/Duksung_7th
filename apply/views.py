from django.shortcuts import render, get_object_or_404, redirect
from .models import Apply
from .forms import ApplyForm
import os
from django.http import HttpResponseRedirect,Http404,HttpResponse
# Create your views here.

def addetail(request,apply_id):
    #applys = apply.objects #쿼리셋 #메소드
    apply_addetail = get_object_or_404(Apply, pk = apply_id)
    return render(request,'addetail.html',{'applys': apply_addetail})
# #다운로드
# def download(request,pk):
#     upload=get_object_or_404(Apply,pk=pk)
#     file_url=upload.file.url[1:]
#     print("a")
#     if os.path.exists(file_url):
#         print("b")
#         with open(file_url,'rb') as fh:
#                 print("c")
#                 response=HttpResponse(fh.read(),content_type="application/octet-stream")
#                 response['attachment']='inline:filename='+os.path.basename(file_url)
#                 print("re == ", response)
#                 return response
#         raise Http404   


# Create your views here.

# 지원하기
def form(request):
    if request.method == "POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.save()
            return redirect('form')
    else:
        form = ApplyForm()
        return render(request, 'form.html', {'form':form})
def adview(request):
    applies = Apply.objects.all()
    return render(request, 'adview.html', {'applies' : applies})
