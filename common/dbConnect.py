import MySQLdb
import mysql.connector

def execute(sql):

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

    cur.execute(sql)
    rows = cur.fetchall()

    # DB操作が終わったらカーソルとコネクションを閉じる
    cur.close()
    conn.close()

    return rows