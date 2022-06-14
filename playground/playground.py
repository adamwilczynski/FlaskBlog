import random
from datetime import datetime

from flask import Flask, make_response, redirect, abort, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)  # Bootstrap is ready to use in templates
moment = Moment(app)


@app.route("/")
def index():
    return render_template("index.html", current_time=datetime.utcnow())


@app.route("/say_hello/<name>")
def say_hello(name):
    return "<h1>Hi, {}. It is so nice to see you here!</h1>".format(name)


@app.route("/cookie")
def cookie():
    response = make_response("<h1>Hello, fellow cookie eater!")
    response.set_cookie("answer", "42")
    return response


@app.route("/random_website")
def random_website():
    return redirect(
        random.choice(
            (
                "https://www.google.com/",
                "https://www.youtube.com/",
                "https://www.gmail.com/",
            )
        )
    )


@app.route("/error")
def error():
    abort(404)  # It raises an exception not returning control to the function


@app.route("/favorite/<int:number>")
def favorite_number(number):
    return render_template("favorite.html", number=number)


@app.route("/show_html/<html>")
def show_html(html):
    return render_template("show_html.html", html=html)
