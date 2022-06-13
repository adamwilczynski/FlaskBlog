# Application Structure

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