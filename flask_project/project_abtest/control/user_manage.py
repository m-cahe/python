from flask_login import UserMixin  #UserMixin: login기능 쉽게 사용 가능
from model.mysql import conn_mysqldb

class User(UserMixin):
    
    def __init__(self, user_id, user_email, blog_id):
        self.id = user_id
        self.user_email = user_email
        self.blog = blog_id
    
    def get_id(self):
        return str(self.id)

    #select
    @staticmethod
    def get(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "select * from user_info where USER_ID = '" + str(user_id) + "'"
        print(sql)

        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        return user
    
    @staticmethod
    def find(user_email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM USER_INFO WHERE USER_EMAIL = '" + str(user_email) + "'"
        print(sql)

        db_cursor.execute(sql)
        user=db_cursor.fetchone()
        if not user:
            return None
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        return user

    #접속이력이 없을때 create
    @staticmethod
    def create(user_email, blog_id):
        user = User.find(user_email)
        if user == None:
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO USER_INFO (USER_EMAIL,BLOG_ID) VALUES ('%s', '%s')" % (str(user_email), str(blog_id))
            db_cursor.execute(sql)
            #user_id는 autoincrement이기 때문에 자동입력
            mysql_db.commit()
            return User.find(user_email)
        else:
            return user

    @staticmethod
    def delete(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM USER_INFO WHERE USER_ID = ('%d')" % (user_id)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted