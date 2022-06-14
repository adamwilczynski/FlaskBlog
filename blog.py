from flask import Flask, render_template

# from flask_bootstrap import Bootstrap

app = Flask(__name__)

# bootstrap = Bootstrap(app)

BLOG_NAME = "EntropistA"


@app.route("/")
def index():
    return render_template("index.html", blog_name=BLOG_NAME)


@app.route("/about")
def about():
    return render_template("about.html", blog_name=BLOG_NAME)


@app.route("/contact")
def contact():
    return render_template("contact.html", blog_name=BLOG_NAME)


@app.route("/post")
def post():
    return render_template("post.html", blog_name=BLOG_NAME)
