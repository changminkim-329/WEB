from django.shortcuts import render
# Create your views here.

import os
def getTemp(request):
    print(os.listdir(os.getcwd()))
    print(os.path.dirname(os.path.realpath(__file__)) )
    return render(request, 'temp.html/')

def getLight(request):
    return render(request, 'light.html/')

def getALert(request):
    return render(request, 'alert.html/')
