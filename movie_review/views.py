
import os, sys

from django.shortcuts import render
from .mdls import working, cvcv
from subprocess import run, PIPE


def index(request):
    return render(request, 'homepage.html')

def index_button(request):
    working.go()
    return render(request, 'homepage.html')

def thispage(request):
    return render(request, 'apage.html')

def apage(request):
    if request.method == request.POST:
        inp = request.POST.get('param')
        out = run([sys.executable,'/media/niketan/cartush/project/major/mdls/cvcv.py',inp],
                  shell=False,stdout=PIPE)
        print(out)
    return render(request, 'apage.html',{'data1': out.stdout})


def analysis(request):
    # analysis page will be defined here
    return render(request, 'analysis.html')


