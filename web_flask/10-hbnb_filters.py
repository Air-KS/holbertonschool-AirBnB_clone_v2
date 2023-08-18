#!/usr/bin/python3
"""Start a Flask web application.

Host = 0.0.0.0, port = 5000
"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage

app = Flask(__name__)
storage.all()

@app.route("/hbnb_filtre", strict_slasher=False)
def filtre(id=None):
    """Comment"""
    data = storage.all(State)
    states = []
    for _ in data:
        states.append(data[_])

    data = storage.all(Amenity)
    amenities = []
    for _ in data:
        amenities.append(data[_])

    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_data(self):
    """refresh data"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
