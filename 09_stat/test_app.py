# Yevgeniy Gorbachev
# SoftDev1 pd1
# K09 -- ’Tis Not a Race -- But You Will Go Faster
# 2019-09-19   

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return open("static/seed.html",'r').read().format(title='Template',body='Yay formatting')

@app.route('/page1')
def page1():
    return open("basic.html",'r').read().format(content="This is the first page. You are trapped here.")

@app.route('/page2')
def page2():
    return "This is the second page. You are trapped here."

@app.route('/my_foist_template')
def template():
    coll = [0,1,1,2,3,5,8]
    return render_template("foist.html",col=coll)
    
if __name__ == "__main__":
    app.debug = True
    app.run()