#Damian Wasilewicz
#SoftDev1 pd6
#K #24: A RESTful Journey Skyward
#2018-11-13
from flask import Flask, render_template
import urllib.request, urllib.parse
import json
app = Flask(__name__)

@app.route("/")
def home():
    '''
    home route, loads nasa api with date, description, title, and url
    '''
    with urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=qeX0r0xhEklQBJPDYhfTZeIdBVDU7hwoYh5cnfEI") as url:
        dict = json.loads(url.read().decode())
    print(dict)
    return render_template('index.html', date = dict['date'],description = dict['explanation'], url = dict['url'], title = dict['title'])

if __name__ == "__main__":
    app.debug = True
    app.run()
