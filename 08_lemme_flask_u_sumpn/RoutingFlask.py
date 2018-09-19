from flask import Flask
app = Flask(__name__)

@app.route("/")
def main_page():
    return "Hello MTV welcome to my crib"

@app.route("/more")
def basic_info():
    return "Hey, you privy devo. This is some more info about me!"

@app.route("/hobbies")
def hobbies():
    return "football big sibs etc"

if __name__ == "__main__":
    app.debug = True
    app.run()
