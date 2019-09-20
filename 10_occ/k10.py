# Yevgeniy Gorbachev
# SoftDev1 pd1
# K10 -- Jinja Tuning
# 20190920

from flask import Flask, render_template
import random
import csv

app = Flask(__name__)

@app.route('/')
@app.route("/occupyflaskst")
def gen_occu():
    return render_template("template.html",title="Jinja tuning",selected=weighted_random(gen_dict()),occs=gen_dict())

def weighted_random(weighted_dict):
    cum_prob = 0
    selected = random.random() * 100
    for key, value in weighted_dict.items():
        cum_prob += value
        if selected < cum_prob:
            return key 
    return "Unemployed"

def gen_dict():
    lines = [line for line in csv.reader(open("./utl/occupations.csv"))]
    lines = [(line[0],float(line[1])) for line in lines[1:-2]]
    return dict(lines)

app.debug = True
app.run()
