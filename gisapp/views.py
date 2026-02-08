from django.shortcuts import render
from django.http import HttpResponse
import sys
from subprocess import PIPE, run
import subprocess
def login_page(request):
    return render(request, 'LoginPage.html')
def home_page(request):
    return render(request, 'Mapview.html')


def Myexternal(request):
    script_path = r"D:/WebAppli/giswebApplciation/giswebApplciation/gisapp/tests.py"
    output = subprocess.check_output([sys.executable, script_path], text=True)
    # currentime = output.strip()
    return render(request, 'Show.html', {'data1': output})
