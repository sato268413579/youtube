from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    import os
    import MySQLdb
    import mysql.connector

    # コネクションの作成
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='password',
        database='youtube_python'
    )

    # DB操作用にカーソルを作成
    cur = conn.cursor(MySQLdb.cursors.DictCursor)

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    # DB操作が終わったらカーソルとコネクションを閉じる
    cur.close()
    conn.close()
    
    return render(request, os.getcwd() + '\youtube\\templates\youtube.html', {'title':'Hello!!!', 'rows': rows})

def submit_post(request):
    return HttpResponse('<h1>OK!<h1/>')