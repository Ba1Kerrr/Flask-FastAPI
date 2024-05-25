from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("useruser.html")


@app.route("/registration/")
def registration():
    return render_template("registration.html")


if __name__ == '__main__':
    app.run(debug=True)
