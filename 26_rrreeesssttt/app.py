#Damian Wasilewicz
#SoftDev1 pd6
#K #26: Getting More REST
#2018-11-15
from flask import Flask, render_template
import urllib.request, urllib.parse
import json
app = Flask(__name__)

@app.route("/")
def home():
    '''
    home route, dog API
    '''
    url = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
    dogdata = json.loads(url.read())
    print(dogdata)

    return render_template('index.html', pic = dogdata['message'])
@app.route("/numbers")
def num():
    '''
    numbers api
    '''
    numUrl = urllib.request.urlopen("http://numbersapi.com/random/trivia")
    numdata = numUrl.read()
    print(numdata)

    return render_template('numbers.html', num = numdata)

@app.route("/cats")
def story():
    '''
    cats api
    '''
    catUrl = urllib.request.urlopen("https://api.thecatapi.com/v1/images/search?size=full&mime_types=jpg&format=json&order=RANDOM&page=0&limit=10&category_ids&x-api-key=bd644ba1-4724-40af-8149-d6cb8973dad3")
    catdata = json.loads(catUrl.read())
    print(catdata)

    return render_template('cats.html', pic = catdata[0]['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
