from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ion')
def ion():
    return render_template("ion.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/polymer")
def polymer():
    return render_template("polymer.html")

@app.route("/history")
def history():
    return render_template("history.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")
