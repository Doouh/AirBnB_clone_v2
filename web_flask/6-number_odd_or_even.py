#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNH!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    text = text.replace("_", " ")
    return 'C '+text


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def show_python(text="is cool"):
    text = text.replace("_", " ")
    return 'Python '+text


@app.route('/number/<int:n>', strict_slashes=False)
def show_int(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_number_odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
