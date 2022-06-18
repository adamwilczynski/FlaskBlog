from flask import Flask, render_template

import post_to_html

app = Flask(__name__)

BLOG_NAME = "EntropistA"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post")
def post():
    return render_template("post.html", content=post_to_html.html)
