#Real Actual Ukranians_Yevgeniy Gorbachev, Ivan Galakhov
#SoftDev1 pd1
#K15 -- Do I Know You?
#2019-10-04

from flask import Flask, render_template, request, session
import os
app = Flask(__name__)

parent = lambda str: str.rfind('/') if str.rfind('/') != -1 else str.rfind('\\') # finds parent directory from string
__ppath__ = __file__[: parent(__file__)] # python file's parent directory

app.secret_key = os.urandom(32)
@app.route('/', methods = ["GET", "POST"])
def index():
    if "username" in session.keys(): # if logged in, welcome page
        return render_template("welcome.html", name=session["username"])
    else: # if not logged in, login page
        return render_template("index.html")

@app.route('/auth', methods = ["GET","POST"])
def auth():
    creds = open(__ppath__ + "/data/creds.txt",'r').read().split('\n') # gets credentials from the file
    if request.form["username"] == creds[0] and request.form["password"] == creds[1]: # if creds are good
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
        return render_template("welcome.html", name=request.form["username"])
    else:
        return render_template("unwelcome.html")

@app.route('/logout')
def deauth():
    del session["username"]
    del session["password"]
    return render_template("index.html")

app.run(debug = True)
