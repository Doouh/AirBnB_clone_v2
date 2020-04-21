#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    if id:
        id = "State.{}".format(id)
    states = storage.all(State)
    cities = storage.all(City)
    return render_template('9-states.html',
                           states=states, cities=cities, id=id)


@app.teardown_appcontext
def close_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
