#Damian Wasilewicz
#SoftDev1 pd6
#K#13: Echo Echo Echo .
#2018-09-27
from flask import Flask, render_template
import urllib.request, urllib.parse
import json

app = Flask(__name__)


@app.route("/")
def home():
    url = urllib.request.urlopen("https://pixabay.com/api/?key=10740974-5ce52855d490768b5fb074d71&q=Julius+Caesar&image_type=photo")
    data = json.loads(url.read())
    pic = data['hits'][0]['largeImageURL']
    print(pic)
    return render_template("home.html", pic = pic)


if __name__ == "__main__":
    app.debug = True
    app.run()
