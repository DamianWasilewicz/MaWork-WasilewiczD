from flask import Flask, render_template
import urllib.request
import json
import ssl
import random

context = ssl._create_unverified_context()

app=Flask(__name__)


@app.route("/")
def google():
#https://www.googleapis.com/customsearch/v1?key=INSERT_YOUR_API_KEY&cx=017576662512468239146:omuauf_lfve&q=lectures

    urlData="https://www.googleapis.com/customsearch/v1?key="
    key="AIzaSyDLFqAoBs-xQCm9XPVAlTsTa0jG8ewM57k"
    urlData2="&cx=009364855531151632334:atzshazndou&q=dog"
    webURL=urllib.request.urlopen(urlData+key+urlData2,context=context)
    data=webURL.read()
    data=json.loads(data)
    print("------------")
    #print(data)
    print(data['items'][0])
    print("-----------")
    title=data['items'][0]['title']
    link = data['items'][0]['link']
    return render_template("google.html",_title=title, url = link)


if __name__ == "__main__":
    app.debug = True
    app.run()
