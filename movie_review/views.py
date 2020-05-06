from django.shortcuts import render
from subprocess import run, PIPE

import os, sys


def index(request):
    return render(request, 'homepage.html')

def index_button(request):
    working.go()
    return render(request, 'homepage.html')

# this is for testing if script run
def thispage(request):
    return render(request, 'apage.html')

def apage(request):
    inp = request.POST.get('param')
    out = run([sys.executable,'/media/niketan/cartush/project/major/mdls/cvcv.py',inp],
              shell=False,stdout=PIPE)
    print(out)
    return render(request, 'apage.html',{'data1': out.stdout})


# will work on this letter
def analysis(request):
    # analysis page will be defined here
    return render(request, 'analysis.html')


