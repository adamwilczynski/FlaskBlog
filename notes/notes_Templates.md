# Templates

## Templates - _Jinja2_

### Variables


```html
<h1>{{ name }}}</h1>
```

### Filters
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

### Control structures

#### Conditional statements
```html
{% if user %}
    Hello, {{ user }}}!
{% else %}}
    Hello, Stranger!
{% endif %}
```

#### Loops
```html
<ul>
    {% for comment in comments %}
        <li>{{comment}}</li>
    {% endfor %}
</ul>
```

#### Macros (function like)
```html
{% macro render_comment(comment) %}
<li>{{ comment }}}</li>
{% endmacro %}

<!-- To make macros reusable store them in standalone files and then import them. -->
{% import "macros.html" as macros %}
```

#### Reusing template code

```html
{% import 'macros.html' as macros %}
<ul>
{% for comment in comments %}
{{ macros.render_comment(comment) }}
{% endfor %}
</ul>
```

```html
{% include "common.html" %}
```

```html
<!-- Replace each block in base.html with given data -->
{% extends "base.html" %}
{% block title}Index{% endblock %}
```

If the content is both in base and derived templates, the derived template is used.

## Bootstrap

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

## Custom error pages

The easiest way is to extend _bootstrap/base.html_ with _base.html_

## Links

Having more than one route and addressing links in the templates
will create dependencies.

The best way to avoid renaming problems is to use Flask
_url_for()_ helper function.

_url_for()_ generates URLs from the information stored in application's URL map.

```python
url_for("index", _external=True)  # Relative path - usage in application
url_for("index", _external=True)  # Absolute path - usage in email
```

## Static files

Special root _/static/\<filename>_ supports static files.

## Flask-Moment

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
<!--super() call makes sure all previous scripts (Bootstrap etc.) are run-->
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}}
```

[Moment.js documentation](https://momentjs.com/docs/) provides information about different formatting options.

