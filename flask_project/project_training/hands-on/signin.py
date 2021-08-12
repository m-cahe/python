from flask import Flask, request, render_template, jsonify
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route("/login", methods=['POST'])
def login_page():
    id = request.form['id']           #html의 Form방식은 form으로 넘겨주기!!! 특히 post방식!!!  #id = request.args.get("id") 로는 안됌
    pw = request.form['pw']
    print(request.url)
    print("id: ",id,"pw: ",pw)
    if id == "idid@google.com":
        data = {"login":"success"}
    else:
        data = {"login":"false"}
    return data 


@app.route("/login_succ", methods=['POST'])
def log_succ():
    #id = request.form['id'] 
    return '<h1>ㅎㅏ이</h1>'
    #render_template('login_succ.html', id)   

#origin
if __name__ == '__main__':
    app.run('127.0.0.1','8080')