from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return open("static/index.html",'r').read()

@app.route('/page1')
def page1():
    return "This is the first page. You are trapped here."

@app.route('/page2')
def page2():
    return "This is the second page. You are trapped here."


if __name__ == "__main__":
    app.debug = True
    app.run()