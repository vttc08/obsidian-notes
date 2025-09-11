Flask Basics

## Installation

```bash
pip install flask
```

## Basic Example

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

## Basic Routing
Flask allows you to define routes using the `@app.route()` decorator. Each route maps a URL to a Python function.

```python
@app.route('/about')
def about():
    return 'This is the About page.'
```

You can also add variables to your routes:

```python
@app.route('/user/<username>')
def show_user(username):
    return f'User: {username}'
```

To specify allowed HTTP methods:

```python
@app.route('/submit', methods=['POST'])
def submit():
    return 'Form submitted!'
```

GET method is the default, so you can omit it if you only want to handle GET requests.
POST method is used for submitting data.

## Running the Application
To run the Flask application, use the following command in your terminal:

```bash
python app.py
```
Make sure to replace `app.py` with the name of your Python file containing the Flask code.