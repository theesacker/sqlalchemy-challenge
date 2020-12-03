import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Setting up database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect = True)
Base.classes.keys()

# We can view all of the classes that automap found
Measurement = Base.classes.measurement
Station = Base.classes.station


#Set up Flask
app = Flask(__name__)

@app.route("/")
def home():
    return(
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/<start>
        /api/v1.0/<start>/<end>
    )

@app.route("/api/v1.0/precipitation")
def precip:
    session = Session(engine)
    #Query Precipitation
    results = session.query(Measurement.date,Measurement.prcp ).\
        filter(Measurement.date > dt.date(2016, 8, 22)).all()
        
        session.close()

        #Convert list of rainfaill to normal list
        total_rainfall = list(np.ravel(results))
        return jsonify(total_rainfall)

@app.route("/api/v1.0/stations")
def w_station:
    session = Session(engine)

    #Query Stations
    results = session.query(Measurement.station)./
    group_by(Measurement.station).count()

    session.close()

    #Convert station list to normal list
    station_list = list(np.ravel(results))



