#  Creating and publishing a Flask Blog Part I

Hi! In this posts' series, I will go through the process of building and deploying a Dynamic Web-Application using **Flask** and **Bootstrap**. **Heroku** will be our deployment platform.

If you are more a backend person and sitting in front of HTML makes you sleepy 😴 - don't discourage yourself yet. We'll use a free, easy to use **Bootstrap** _Clean Blog_ template.

In the first part of the tutorial, we will focus on creating MVP (Minimum viable product) - a basic app using bare Flask and uploading it to Heroku. After that, everyone on the web will be able to see our result and listen to you bragging about the newly acquired coding skills 😎

## Creating project files

Create a new project folder and name it (in my case, _FlaskBlog_). Inside it create files:
 - `README.md` (for documentation)
 - `blog.py` (Flask app)
 
Folders:
 - `static`
 - `templates`
 
```
FlaskBlog
│   README.md
│	blog.py
└───static   
└───templates
```

## Installing Flask
```terminal
pip install flask
```

## Publishing project on GitHub

After creating a basic file structure, let's publish the project so that we can track each of the changes made.

First initiate a local repository inside project directory.
```terminal
git init
git add static templates blog.py README.md
git commit -m "Created file structure"
```

Next, create an empty repository on GitHub
https://github.com/new

Then link your project with just created GitHub repository.
```terminal
git remote add origin [repository_link]
git push -f origin master
```

repository_link was in my case https://github.com/EntropistA/FlaskBlogExample.git

Each time you make changes to the project, follow a standard commit  steps.
```terminal
git add [file_that_changed]
git commit -m [commit_message]
git push origin master
```

## Basic Flask App

```python
from flask import Flask  
  
# Dunder variable __name__ contains app location in your file system  
app = Flask(__name__)  
  
  
@app.route('/')  # Routing decorator  
def index():  # Decorated function returning HTML code  
  return "Hello, world!"
```

Yes. That's it! Considering how short this code is, let's name only a few things here.
### routing decorator 
Takes a path relative to your webpage domain. Leaving it with "/" tells that the function following it will return main page (e.g. entropista.tech) HTML.

### index
 function following the decorator may have any name, but the convention states that it's name should be the part of the website it is referring to. As we define what happens on the main page it's name becomes _index_ (which is HTML default document name).

### return value
Although no HTML tags are present Flask will move our string `Hello, world!` to the body section of the displayed page. We'll see that in the next step.

## Running debug server

Windows cmd commands:
```terminal
SET FLASK_APP=blog.py
SET FLASK_DEBUG=1
flask run
```
Linux and Mac:
```terminal
export FLASK_APP=blog.py
export FLASK_DEBUG=1
flask run
```

First, we specify a file containing our Flask _app_ variable. Then we turn on debug mode to update our server after each change that we make. Finally, we run our app and get a link to the working server, which we can open in the browser. We can see our "_Hello, world!_" message and server responding to the changes in return message after refreshing the page. 

## Heroku integration

Now as we have our debug server up and running, it's time to show our work to the world.

### Connecting Heroku Profile with GitHub

First, if you don't already have a **Heroku** account, create one:
https://signup.heroku.com/login

Next, head over to the profile section in the right upper corner.

Then go to:
Applications → Third-party Services → Connect with a GitHub profile

After following those steps, the result should be as follows:

![connecting heroku to github acoount](https://i.ibb.co/tJjktqj/connecting-heroku-to-github-acoount.jpg)
### Command Line Interface Download

Now it's time to download **Heroku CLI** - _devcenter_ provides a great tutorial, so I will just point you to it. Follow your system's download process and **remember to add CLI to the PATH** for ease of use in the terminal. In my case, there had been a **restart required** before the terminal recognized Heroku commands.

https://devcenter.heroku.com/articles/heroku-cli

After performing the last command from the tutorial, which is:

```terminal
heroku create
```

Go to your _dashboard_ in the browser. The newly created app should appear.

https://dashboard.heroku.com/apps

### Linking Heroku app with a GitHub repository

In your profile's _dashboard_, click on the newly created app. Head over to _Deploy_, select GitHub as a _Deployment method_ and search for a repository to connect to.

![Linking Heroku app with GitHub repo](https://i.ibb.co/p0LyW0v/link-heroku-app-with-github-repo.jpg)
When asked, select that the Heroku app should respond to each change you make to the GitHub project.

## Adding Server Functionality to our code

### Installing Gunicorn

For as far as Flask lets us to render web pages and route users. We need a server to handle the very back-end of our app. In this place comes the **gunicorn** - _a Python WSGI HTTP Server for UNIX_.

Its installation is pretty straightforward.

```terminal
pip install gunicorn
```

After pip has installed **gunicorn** we need 2 additional files for our server to work.

### requirements.txt

Here, as well, pip comes in very handy. The following command will store all of the files in `requirements.txt` file. The physical server provided by Heroku will look inside it and install all the dependencies (modules which our project requires in order to run).

```terminal
pip freeze > requirements.txt
```

### Procfile

The second file is needed by gunicorn. What's important is that it has **no extension**. Inside it there should be a one line:

`web: gunicorn <file_name>:<flask_app_variable_name>`

In our case:

```
web: gunicorn blog:app
```

`blog.py` is the file in which we store Flask application variable which is used with the name of _app_ in our code:

```python
...
app = Flask(__name__)
...
```

## Pushing changes

Now push all the changes made to the project's GitHub repository.

## Congratulations!

Although your app currently only shows 13 letters on the screen, the possibilities are infinite!

What if you had templates with HTML code to display?
Wouldn't it be amazing to render contents of the web page using advanced multi-line Python functions?
What can you say to dynamically responding to user actions using forms? 

We will cover those in the future tutorials. Stay tuned!

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkzNjA2NTk4MSwxMjE3MTgwMzI3LDg1NT
Y4NDUzXX0=
-->