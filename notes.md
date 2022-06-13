# FlaskBlog Notes

## Keywords

business logic -
use real world business rules to determine how data can be created, stored, changed

presentation logic -
front end, how objects are displayed to users

rendering - replacing variables with actual values

## Routing

- make_response()
- render_template()

- abort()

## The first application

```python
# __name__ parameter passes project name and file location to Flask
app = Flask(__name__)
```

## Terminal commands

```commandline
set FLASK_APP=hello.py
set FLASK_DEBUG=1

flask run

# All computers in the network can connect
flask run --host 0.0.0.0
```

_set_ command is replaced by _export_ on Linux

## Debug mode

Consists of 2 modules:
1. reloader
2. debugger

## Context globals

- current_app - active app
- g - temporary storage using dot notation (dict like)
- request - contents of client request
- session - user session, store values remembered between requests

## Hooks
- before_request
- before_first_request (server initialization)
- after_request
- teardown_request
(function to run after each request even if unhandled exceptions occurred)

## Extensions

### Templates - _Jinja2_

#### Variables


```html
<h1>{{ name }}}</h1>
```

#### Filters
- safe - without escaping
- capitalize
- lower
- upper
- title
- trim - removes trailing whitespace
- striptags

```html
<h1>{{ name|capitalize }}}</h1>
```

#### Control structures

##### Conditional statements
```html
{% if user %}
    Hello, {{ user }}}!
{% else %}}
    Hello, Stranger!
{% endif %}
```

##### Loops
```html
<ul>
    {% for comment in comments %}
        <li>{{comment}}</li>
    {% endfor %}
</ul>
```

##### Macros (function like)
```html
{% macro render_comment(comment) %}
<li>{{ comment }}}</li>
{% endmacro %}

<!-- To make macros reusable store them in standalone files and then import them. -->
{% import "macros.html" as macros %}
```

##### Reusing template code

```html
{% include "common.html" %}

<!-- Replace each block in base.html with given data -->
{% extends "base.html" %}
{% block title}Index{% endblock %}
```

If the content is both in base and derived templates, the derived template is used.

### Bootstrap

```python
pip install flask-bootstrap
```

Bootstrap is an open-source web browser client-side framework.

base.html is created by _Flask-Bootstrap_

Mandatory blocks:
- title
- navbar
- content

There are additional blocks as well.
 
```html
{% extends "bootstrap/base.html" %}
```

### Custom error pages

The easiest way is to extend _bootstrap/base.html_ with _base.html_

### Links

Having more than one route and addressing links in the templates
will create dependencies.

The best way to avoid renaming problems is to use Flask
_url_for()_ helper function.

_url_for()_ generates URLs from the information stored in application's URL map.

```python
url_for("index", _external=True)  # Relative path - usage in application
url_for("index", _external=True)  # Absolute path - usage in email
```

### Static files

Special root _/static/\<filename>_ supports static files.

### Flask-Moment

```commandline
pip install flask-moment
```

Flask-Moment provides an elegant solution that allows the server to work exclusively in UTC.
It uses _Moment.js_ and _jQuery.js_ (which Bootstrap already includes) libraries.

```python
from flask_moment import Moment
moment = Moment(app)
```

```html
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}}
```

