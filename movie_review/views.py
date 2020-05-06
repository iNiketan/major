import keras
import numpy as np
import pandas as pd
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import cv2
import pickle
import h5py
import datetime
import os

from django.shortcuts import render
from .mdls import working, cvcv
from subprocess import run, PIPE


def index(request):
    return render(request, 'homepage.html')

def index_button(request):
    working.go()
    return render(request, 'homepage.html')

def analysis(request):
    # analysis page will be defined here
    return render(request, 'analysis.html')

def thispage(request):
    return render(request, 'apage.html')


def apage(request):
    info = request.POST
    out = run()

    return render(request, 'apage.html')
