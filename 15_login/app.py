#AnIOop_Joseph Lee, Ray Lee, Yevgeniy Gorbachev
#SoftDev1 pd1
#K15 -- Do I Know You?
#2019-10-04

from flask import Flask, render_template, request

app = Flask(__name__)

parent = lambda str: str.rfind('/') if str.rfind('/') != -1 else str.rfind('\\') # finds parent directory from string
__ppath__ = __file__[: parent(__file__)] # python file's parent directory

@app.route('/')
def login():
    if 'username' in session:
        username = session[username]