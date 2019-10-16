# SeQL_Yevgeniy Gorbachev, Ethan Joo, Eric Lau
# SoftDev1 pd1
# K21(?) -- **?
# 2019-10-??

from flask import Flask, request, render_template, session, url_for

app = Flask(__name__)

# Welcome/index page
@app.route('/', methods = ['GET', 'POST'])
@app.route('/welcome', methods = ['GET', 'POST']) 
def index():
    return

# Article from pages
@app.route('/pages/<page>', methods = ['GET', 'POST'])
def get_page(page):
    return

# Using content from page entry, generates edit mode
@app.route('/pages/<page>/edit', methods = ['POST'])
def edit(page):
    return

# search for pages
@app.route('/search', methods = ['POST'])
def search():
    return

# create account
# if GET, returns default registration page
# if POST, updates user db
@app.route('/register', methods = ['GET', 'POST'])
def register():
    return


################ ACTION ROUTES ################
# action routes perform an action, then redirect to some page

# login action
@app.route('/auth', methods = ['POST'])
def auth():
    return

# logout action
@app.route('/deauth', methods = ['POST'])
def deauth():
    return

# globally save changes to page
@app.route('/commit', methods = ['POST'])
def commit():
    return

