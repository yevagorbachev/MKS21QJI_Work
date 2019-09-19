# Yevgeniy Gorbachev
# SoftDev1 pd1
# K8 -- First Flask App
# 2019-09-19   

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return open("static/index.html",'r').read()

@app.route('/page1')
def page1():
    return open("templates/basic.html",'r').read().format(content="This is the first page. You are trapped here.")

@app.route('/page2')
def page2():
    return "This is the second page. You are trapped here."


if __name__ == "__main__":
    app.debug = True
    app.run()