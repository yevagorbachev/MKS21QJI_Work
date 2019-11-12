#Yevgeniy Gorbachev
#SoftDev1 pd1
#K24 -- A RESTful Journey Skyward
#2019-11-13

from flask import *
import urllib.request
import json
from os import urandom

__key__ = '5Vrh42prZ7Y2kxrO0KAH6fQ0CqpN5tDujnmZk8sF'
__url__ = f'https://api.nasa.gov/planetary/apod?api_key={__key__}'

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route('/')
def index():
    request = urllib.request.urlopen(__url__)
    response = request.read()
    data = json.loads(response)
    return render_template('index.html',img_url=data['url'])

# if __name__ == 'main':
app.run(debug=True)
