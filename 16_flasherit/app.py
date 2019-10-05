#Real Actual Ukranians_Yevgeniy Gorbachev, Ivan Galakhov
#SoftDev1 pd1
#K16 -- Oh yes, perhaps I do...
#2019-10-07

from flask import Flask, render_template, request, session
import os

app = Flask(__name__)

parent = lambda str: str.rfind('/') if str.rfind('/') != -1 else str.rfind('\\') # finds parent directory from string
__ppath__ = __file__[: parent(__file__)] # python file's parent directory

app.secret_key = os.urandom(32)
__creds__ = {
    'username':'putin',
    'password':'soviet_glory'
}


@app.route('/', methods = ['GET','POST'])
def index():
    if 'username' in session.keys():
        return Flask.redirect(Flask.url_for(welcome))
    else:
        return render_template('login.html', title = 'Login')

@app.route('/welcome', methods = ['GET','POST'])
def welcome():
    return render_template('welcome.html', name = session['username'], title = 'Welcome!')

@app.route('/error', methods = ['GET','POST'])
def error(fails):
    return render_template


@app.route('/auth', methods = ['POST'])
def auth():
    fails = [item[0] for item in __creds__.items() if not (item[1] == __creds__[item[0]])]
    if len(fails) == 0:
        session['username'] = request.form['username']
        return Flask.redirect(Flask.url_for(index))
    else:
        failstr = " and ".join(fails)
        return Flask.redirect(Flask.url_for(error))

@app.route('/deauth', methods = ['GET', 'POST'])
def deauth():
    del session['username']
    return Flask.redirect(Flask.url_for(index))
