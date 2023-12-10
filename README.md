# SQLALCHEMY Challenge

## Overview
This repository examines climate data from measurement stations around Hawaii. It utilizes sqlalchemy and sqlite to analyze the data from the database (Hawaii.sqlite)["SurfsUpResources/hawaii.sqlite"]. It then takes the data, and creates an API with Flask to serve various queries to the end user.  

This database contains two tables:

<ul>
<li><a href="SurfsUp/Resources/hawaii_stations.csv">hawaii_stations:</a> outlies each of the 9 measurement stations by station id, name, latitude, longitde, and elevation, with the dataset</li>
<li><a href="SurfsUp/Resources/hawaii_measurements.csv">hawaii_measurements:</a> contains measurements from all stations and lists the date, precipitation(in inches) and temperature (in degrees F) of each measurement</li>
</ul>

## Part 1 -- Climate and Station Analysis:

This section uses SqlAlchemy to analyze the above database. The code can be found in the file: (climate_analysis)["SurfsUp/climate_analysis.ipynb"].

### Climate Data Analysis

In the above file, the data is first analyzed for climate data. First, an sqlalchemy engine is created for the sqlite database, then is reflected into a model. Each table is saved as a refrence variable and a session is begun to query the database to answer the following questions:

<ol>
    <li>What is the most recent date in the measurment table? <i>(2017-08-23)</i></li>
    <li>What are the precipitation measurements for the most recent 12 month period?</li>
</ol>

This precipitation data was then converted to a pandas dataframe, and charted. The resulting chart can be found in (precipitation_chart)['SurfsUp/visualizations/precipitation_chart.png']

This dataframe was also summarized in the following table:

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>precipitation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2021.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.177279</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.461190</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.020000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.130000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>6.700000</td>
    </tr>
  </tbody>
</table>
</div>

### Exploratory Station Analysis

The following questions were queried from the database to examine the individual measurement stations:

<ol>
    <li>How many stations are in the dataset? <i>(9)</i></li>
    <li>How many measureents came from each station?</li>
    <li>Which station had the most measurements? <i>USC00519281</i></li>
</ol>

Based on the most active station from the above query, the following queries were executed:

<ol>
    <li>What are the Minimum, Maximum, and Average Temperatures from this measurement station?<i>(53.0F, 87.0F, 71.7F)</i></li>
    <li>What are the temperatures for the most recent 12 months?</li>
</ol>

A histogram was then created from the 12 month temperature data. This histogram can be found in the (temp_distribution)['SurfsUp/visualizations/temp_distribution.png'] file.

## Part 2: Climate App

In this section a Flask API was designed based on the previous queries in section 1. This app can be found in the file: (app.py)['SurfsUp/app.py']

Four routes were created for this API, with the following content:

<ol>
<li>"/" : returns a list all the available routes</li>
<li>"/api/v1.0/precipitation": returns a jasonified dictionary of query results from the precipitation analysis</li>
<li>"/api/v1.0/stations": returns a JSON list of stations from the dataset</li>
<li>"/api/v1.0/tobs": returns the temperature observations of the most-active station for the previous year of data.
<li>"/api/v1.0/<start>": returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature beginning at a specified 
<li>"api/v1.0/<start>/<end>": returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start-end range.</li>
</ol>
