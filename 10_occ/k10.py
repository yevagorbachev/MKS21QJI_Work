# Yevgeniy Gorbachev
# SoftDev1 pd1
# K10 -- Jinja Tuning
# <ISO 8601 date>

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route("/occupyflaskst")
def gen_occu():
    