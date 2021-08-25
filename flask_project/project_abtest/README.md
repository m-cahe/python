### blog_abtest.py
 - blueprint
 - LoginManager() <br>
      - From flask_login import LoginManager <br>
      login_manager = LoginManager() <br>
      login_manager.init_app(app) <br>
 - app.before_request 

### view > blog.py
  - /set_page
     - /set_email
       - request.form['user_id'], request.form['user_email']  --> mysql 에 insert
       - login_user
     - session저장, 세션 불러온 후 페이지 리턴
  - /logout
     - logout_user()
  - /deletelog
     -  mysqld이용 delete  
