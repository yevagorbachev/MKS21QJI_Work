#Real Actual Ukranians_Yevgeniy Gorbachev, Ivan Galakhov
#SoftDev1 pd1
#K16 -- Oh yes, perhaps I do...
#2019-10-07

from flask import Flask, render_template, request, session, redirect, url_for
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
        return redirect(url_for('welcome'))
    else:
        return render_template('login.html', title = 'Login')

@app.route('/welcome', methods = ['GET','POST'])
def welcome():
    return render_template('welcome.html', name = session['username'], title = 'Welcome!')

@app.route('/error', methods = ['GET','POST'])
def error():
    failstr = session['failstr']
    del session['failstr']
    return render_template('error.html', fails = failstr, title = 'error')





@app.route('/auth', methods = ['POST'])
def auth():
    inputs = {
        'username':request.form['username'],
        'password':request.form['password']
    }
    fails = [item[0] for item in inputs.items() if item[1] != __creds__[item[0]]]
    if len(fails) == 0:
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        failstr = " and ".join(fails)
        session['failstr'] = failstr
        return redirect(url_for('error'))
        
@app.route('/deauth', methods = ['POST'])
def deauth():
    del session['username']
    return redirect(url_for('index'))

app.run(debug = True)