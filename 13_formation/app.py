from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/auth")
def authenticate():
    print(app)
    #gets arguments from request, which contains inputted information
    print(request)
    #info stored in immutable dictionary request
    print(request.args)
    print(request.headers)
    return render_template("user.html",
                            first = request.args['first'],
                            last = request.args['last'],
                            request = request.method)


if __name__ == "__main__":
    app.debug = True
    app.run()
