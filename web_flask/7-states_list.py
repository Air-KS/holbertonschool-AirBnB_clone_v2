#!/usr/bin/python3
"""Start a Flask web application.

Host = 0.0.0.0, port = 5000
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """return all states in the db"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_data(self):
    """refresh data"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
