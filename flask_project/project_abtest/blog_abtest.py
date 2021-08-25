from flask import Flask, jsonify, request, render_template, make_response, session
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from view import blog
from control.user_manage import User
import os 


#os: 소셜로그인을 사용할 때 http에서도 test가능하도록 os라는 기능 을 붙임

#LoginManager: 세션관리 등록, current_user: user정보 언제든 참조 가능, login_required : 로그인이 된 사용자만 access 가능,login_user logout_user: 로그인 로그아웃시 세션관리

#https만을 지원하는 기능을 http에서 실행할 때 필요한 기능
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'secure_key'

app.register_blueprint(blog.blog_test, url_prefix='/blog') #app.register_blueprint(클래스.객체, 기본url='/url주소')
login_manager = LoginManager()
login_manager.init_app(app)  #login_manager에 앱 등록 필요
login_manager.session_protection = 'strong'

@login_manager.user_loader     #로그인 시 session 확인해서 id 기반의 객체 불러와야 함
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler  #로그인 안된 사용자가 로그인한 사용지만 이용가능한 api에 접근했을 때
def unathourized():
    return make_response(jsonify(success=False), 401)

#app이 실행되기 전마다 실제 ip정보 얻기
@app.before_request     
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)


if __name__ == '__main__':
    app.run(host ='127.0.0.1', port ='8080', debug=True)


#blog_abtest.py: 서버구동, login 여부 파악 + 세션관리(login_manager.user_loader)
#template: 필요한 html페이지
#view: html페이지 route 설정

# blue print