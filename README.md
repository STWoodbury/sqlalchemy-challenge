# SQLALCHEMY Challenge

## Overview
This repository examines climate data from measurement stations around Hawaii. It utilizes sqlalchemy and sqlite to analyze the data from the database (Hawaii.sqlite)[Resources/hawaii.sqlite]. It then takes the data, and creates an API with Flask to serve various queries to the end user.  

This database contains two tables:

<ul>
<li><a href="Resources/hawaii_stations.csv">hawaii_stations:</a> outlies each of the 9 measurement stations by station id, name, latitude, longitde, and elevation, with the dataset</li>
<li><a href="Resources/hawaii_measurements.csv">hawaii_measurements:</a> contains measurements from all stations and lists the date, precipitation(in inches) and temperature (in degrees F) of each measurement</li>
</ul>

## Part 1 -- Climate and Station Analysis:

This section uses SqlAlchemy to analyze the above database. The code can be found in the file: (climate_analysis)['climate_analysis.ipynb].

### Climate Data Analysis

In the above file, the data is first analyzed for climate data. First, an sqlalchemy engine is created for the sqlite database, then is reflected into a model. Each table is saved as a refrence variable and a session is begun to query the database to answer the following questions:

<ol>
    <li>What is the most recent date in the measurment table? <i>(2017-08-23)</i></li>
    <li>What are the precipitation measurements for the most recent 12 month period?</li>
</ol>

This precipitation data was then converted to a pandas dataframe, and charted. The resulting chart can be found in (precipitation_chart)['visualizations/precipitation_chart.png']

This dataframe was also summarized in the following table:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
