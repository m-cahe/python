import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST
    ,port=3306
    ,user='hello'
    ,passwd='hellomysql'
    ,db='blog_db'
    ,charset='utf8'
)

def conn_mysqldb():
    if not MYSQL_CONN.open:         #connection 끊어졌을 때 다시 시작
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN