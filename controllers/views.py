from django.http import HttpResponse
from django.shortcuts import render
from ..common import viewRender, dbConnect

def index(request):
    rows = dbConnect.execute("SELECT * FROM users")

    userId = "kazumasato"

    thumbnails = dbConnect.execute("SELECT * FROM media where login_id = '" + userId + "'")
    user = dbConnect.execute("SELECT * FROM users where login_id = '" + userId + "'")
    print(user[0])
    return viewRender.viewRender(request, 'youtube.html', {'title':'Hello!!!', 'rows': rows, 'thumbnails': thumbnails})

def submit_post(request):
    return HttpResponse('<h1>OK!<h1/>')