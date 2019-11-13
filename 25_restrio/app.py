#Yevgeniy Gorbachev
#SoftDev1 pd1
#K24 -- A RESTful Journey Skyward
#2019-11-13

from flask import *
import urllib.request
from urllib.parse import quote
import json
from os import urandom

class API(object):
    key: str
    url: str
    def __init__(self, key, url):
        self.key = key
        self.url = url
    
    def get_url(self, query="") -> str:
        query = quote(query)
        return self.url.format(_key = self.key, _query = query)
    
WOLFRAM = API('P4747E-2545R4KKGK', 'http://api.wolframalpha.com/v2/query?appid={_key}&input={_query}&output=json')

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route('/')
def index():
    query = 'tides in seattle'
    query_link = WOLFRAM.get_url(query)
    print(query_link)

    request = urllib.request.urlopen(query_link)
    response = request.read()
    data = json.loads(response)
    return render_template('index.html',api_data=str([item for item in data['queryresult'].items()]))

# if __name__ == 'main':
app.run(debug=True)
