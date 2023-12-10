# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
#home route
@app.route("/")
def home():
    
    #List all available api routes.
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )
 
 #precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create session from Python to the DB
    session = Session(bind=engine)
    
    # query preciitation from measurements
    results = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= '2016-08-23').\
    order_by(measurement.date.desc()).all()
    
    #close the session
    session.close()
    
    # convert to a list of dictionaries with date as key and prcp as value
    all_dates = []
    for date, prcp in results:
        dict = {date:prcp}
        all_dates.append(dict)
    
    # return jsonified results
    return(jsonify(all_dates))

# stations route 
@app.route("/api/v1.0/stations")
def stations():

    # create session from Python to the DB
    session = Session(bind=engine)

    # query stations 
    stations = session.query(station.station).all()

    #close the session
    session.close()

    # ravel to list
    station_list = list(np.ravel(stations))
    
    # return the list
    return jsonify(station_list)

# tobs route
@app.route("/api/v1.0/tobs")
def tobs():

     # create session from Python to the DB
    session = Session(bind=engine)

    # query the dates and temperature observations of the most-active station for the previous year of data.
    active_station_temps = session.query(measurement.tobs).\
    filter(measurement.date >= '2016-08-23').\
    filter(measurement.station == 'USC00519281').all()

    #close the session
    session.close()

     # ravel to list
    tobs_list = list(np.ravel(active_station_temps))
    
    # return the list
    return jsonify(tobs_list)

# start route
@app.route("/api/v1.0/<start>")
def start_route(start):

    # create session from Python to the DB
    session = Session(bind=engine)

    # query the min, avg and max temps from the start date
    results = session.query(func.Min(measurement.tobs), func.Avg(measurement.tobs), func.Max(measurement.tobs)).\
        filter(measurement.date >= start).all()

     #close the session
    session.close()

    # add results to dictionary
    for min, avg, max in results:
        results_dict = {'min_temp':min,'avg_temp':avg, 'max_temp':max}

   #return jsonified dictionary
    return jsonify(results_dict) 

# start/end route
@app.route("/api/v1.0/<start>/<end>")
def start_end_route(start, end):

    # create session from Python to the DB
    session = Session(bind=engine)

    # query the min, avg and max temps from the start date
    results = session.query(func.Min(measurement.tobs), func.Avg(measurement.tobs), func.Max(measurement.tobs)).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()

     #close the session
    session.close()

    # add results to dictionary
    for min, avg, max in results:
        results_dict = {'min_temp':min,'avg_temp':avg, 'max_temp':max}

   #return jsonified dictionary
    return jsonify(results_dict) 

if __name__ == '__main__':
    app.run(debug=True)