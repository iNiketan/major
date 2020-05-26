from django.shortcuts import render
from subprocess import run, PIPE

import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def index(request):
    return render(request, 'homepage.html')


def instructions(request):
    return render(request, 'instruction.html')

# for the movie_play and working page
def movies_page(request):
    return render(request, 'movie_play.html')

def movie_play_button(request):
    file_path = "mdls/working.py"
    u = os.path.join(BASE_DIR, file_path)
    out = run([sys.executable, u], shell=False, stdout=PIPE)
    return render(request, 'movie_play.html', {'modelfile': out.stdout})

# this button run analysis.py and render analysis page
def movie_analysis_button(request):
    file_path = "mdls/analysis.py"
    u = os.path.join(BASE_DIR, file_path)
    out = run([sys.executable, u], shell=False, stdout=PIPE)
    return render(request, 'analysis_page.html', {'imgfile': out.stdout})

# show the analysis and score page
def analysis(request):
    # analysis page will be defined here
    return render(request, 'analysis_page.html')


