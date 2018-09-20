from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("base.html")



@app.route("/more")
def basic_info():
    return render_template("info.html")

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
