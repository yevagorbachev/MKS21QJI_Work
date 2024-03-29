#Yevgeniy Gorbachev
#SoftDev1 pd1
#K25 -- Getting More REST
#2019-11-14

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
    # Wolfram's API
    return get_wolfram('weather in new york')

def get_wolfram(query=''):
    query_link = WOLFRAM.get_url(query)
    request = urllib.request.urlopen(query_link)
    response = request.read()
    data = json.loads(response)['queryresult']
    img = data['pods'][0]['subpods'][0]['img']
    return render_template('img.html',img_title = img['title'], img_link = img['src'])


app.run(debug=True)
