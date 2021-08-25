from flask import Flask, Blueprint, request, render_template,jsonify, redirect, url_for, session
from flask.globals import current_app, session
from flask.helpers import make_response
from flask_login import login_user, current_user
from flask_login.utils import logout_user
from control.user_manage import User
from control.session_manage import BlogSession
import datetime


blog_test = Blueprint('blog',__name__)

@blog_test.route('/set_email', methods=['GET','POST'])
def set_email():
    if request.method == 'GET':
        print('user_email: ' , request.args.get('user_email'))
        return redirect('/blog/set_page')
            #redirect(url_for('blog.test_blog'))
    else:
        #print('user_email_header: ', request.headers)
        print('user_email: ', request.form) #출력>>>> user_email:  ImmutableMultiDict([('user_email', 'abc@google.com'), ('blog_id', 'A')])
        user = User.create(request.form['user_email'],request.form['blog_id'])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))     # 1년동안 session정보 저장
        return redirect('/blog/set_page') #set_page 호출

@blog_test.route('/set_page')
def set_page():
    if current_user.is_authenticated:  #세션정보서 id를 호출, id가 허용된 사용자일때  #current_user:blog_abtest의 user_loader에서 가져옴
        webpage = BlogSession.get_blog_page(current_user.blog)
        BlogSession.save_session_info(session['client_id'], current_user.user_email, webpage)
        return render_template(webpage, user_email = current_user.user_email)  #user_email 변수에 파라미터 넣어서 전달
    else:
        webpage = BlogSession.get_blog_page()
        BlogSession.save_session_info(session['client_id'], 'anonymous', webpage)
        return render_template(webpage)

@blog_test.route('/logout')
def logout():
    logout_user()
    return redirect('/blog/set_page') 

#구독취소(=탈퇴)
@blog_test.route('/deletelog')
def deletelog():
    print('current_user: ', current_user.id, current_user.user_email, current_user.blog)
    User.delete(current_user.id)
    logout_user()
    return redirect('/blog/set_page') 


