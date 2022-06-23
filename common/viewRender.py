from django.http import HttpResponse
from django.shortcuts import render
import os

def viewRender(request, viewName, option):
    return render(request, os.getcwd() + '\youtube\\templates\\' + viewName, option)