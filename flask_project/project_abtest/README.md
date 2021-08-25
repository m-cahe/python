### 1. blog_abtest.py
 - blueprint
 - LoginManager() <br>
      - From flask_login import LoginManager <br>
      login_manager = LoginManager() <br>
      login_manager.init_app(app) <br>
 - app.before_request 

### 2. model > mongodb.py, mysql.py
 - DB접속 및 DataBase와 연결

### 3. control > session_manage
 - mongodb
 - @staticmethod
    - get_blog_page(__) : A,B 페이지 순차출력/구독한 페이지 리턴

### 4. control > user_manage
 - mysql
 - @staticmethod
    - User클래스 
    - @staticmethod
     - CRUD
     -  mysql_db = conn_mysqldb() <br>
        db_cursor = mysql_db.cursor() <br>
        sql = "sql문" <br>
        db_cursor.execute(sql) <br>
        mysql_db.commit() <br>

### 5. view > blog.py
  - ../ set_page
     - ../set_email
       - request.form['user_id'], request.form['user_email']  --> mysql 에 insert
       - login_user
     - session저장, 세션 불러온 후 페이지 리턴
  - ../ logout
     - logout_user()
  - ../ deletelog
     -  mysqld이용 delete  
