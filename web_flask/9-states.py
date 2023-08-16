#!/usr/bin/python3
"""Start a Flask web application.

Host = 0.0.0.0, port = 5000
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
        States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_data(self):
    """refresh data"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
