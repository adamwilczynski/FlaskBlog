import flask
from flask import Flask, render_template

app = Flask(__name__)

BLOG_NAME = "EntropistA"


@app.route("/")
def index():
    return render_template("index.html", blog_name=BLOG_NAME)


@app.route("/about")
def about():
    response = flask.Response(render_template("about.html", blog_name=BLOG_NAME))
    response.headers['Content-Type'] = "text/css; charset=utf-8"
    return response


@app.route("/contact")
def contact():
    return render_template("contact.html", blog_name=BLOG_NAME)


@app.route("/post")
def post():
    return render_template("post.html", blog_name=BLOG_NAME)
