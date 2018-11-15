#Damian Wasilewicz
#SoftDev1 pd6
#K #25: Getting More REST
#2018-11-14
from flask import Flask, render_template
import urllib.request, urllib.parse
import json
app = Flask(__name__)

@app.route("/")
def home():
    '''
    home route, jservice API
    '''
    url = urllib.request.urlopen("http://jservice.io/api/random")
    data = json.loads(url.read())
    #print(data)

    return render_template('index.html', question = data[0]['question'], answer = data[0]['answer'], airdate = data[0]['airdate'], difficulty = data[0]['value'],category = data[0]['category']['title'])

if __name__ == "__main__":
    app.debug = True
    app.run()
