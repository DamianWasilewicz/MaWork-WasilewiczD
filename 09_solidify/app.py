from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello MTV welcome to my crib"

if __name__ == "__main__":
    app.debug = True
    app.run()
