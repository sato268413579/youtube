from django.http import HttpResponse
from django.shortcuts import render
from ..common import viewRender, dbConnect
import os
import MySQLdb
import mysql.connector

def detail(request):
    media_detail = dbConnect.execute("select * from media where id = " + request.GET.get("media_id"))[0]
    return viewRender.viewRender(request, 'media_detail.html', {"media_detail": media_detail})

def upload_file_select(request):
    return viewRender.viewRender(request, 'media_select.html', {})