import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask_sqlalchemy_session import flask_scoped_session
from cgi import escape

#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///titanic.sqlite", connect_args={'check_same_thread': False})
engine = create_engine("sqlite:///titanic.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger

# Create our session (link) from Python to the DB
sessionfactory = sessionmaker(bind=engine)
# Session = scoped_session()


# session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
session = flask_scoped_session(sessionfactory, app)


#################################################
# Flask Routes
#################################################

# @app.route("/")
# def welcome():
#     """List all available api routes."""
#     return (
#         f"Available Routes:<br/>"
#         f"/api/v1.0/names<br/>"
#         f"/api/v1.0/passengers"
#     )
# Home route
@app.route("/")
def welcome():
   return (
       f"<html><body><h1>Welcome to my Climate Application API!</h1><br/>"
       f"<h2>Available Routes:</h2><br/></body></html>"
       f"/api/precipitation<br/>"
       f"/api/stations<br/>"
       f"/api/temperature<br/>"
       f"/api/daterange/" + escape("<start_date>") + "<br/>"
       f"/api/daterange/&ltstart_date&gt<br/>"
       f"/api/daterange/" + escape("<start_date>") + "/" + escape("<end_date>") + "<br/>"
   )


@app.route("/api/v1.0/names")
def names():
    """Return a list of all passenger names"""
    # Query all passengers
    # session = scoped_session(sessionfactory)
    results = session.query(Passenger.name).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/passengers")
def passengers():
    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    # session = scoped_session(sessionfactory)
    results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
