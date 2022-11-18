# US_Bikeshare_DA_python
In this project, we made use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. We wrote code to import the data and answer interesting questions about it by computing descriptive statistics. We also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

<b>Bike Share Data</b>

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

<b>The Datasets</b>

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
<ul>
<li> Start Time (e.g., 2017-01-01 00:07:57) </li>
<li> End Time (e.g., 2017-01-01 00:20:53) </li>
<li> Trip Duration (in seconds - e.g., 776) </li>
<li> Start Station (e.g., Broadway & Barry Ave)</li>
<li> End Station (e.g., Sedgwick St & North Ave) </li>
<li> User Type (Subscriber or Customer) </li>
</ul>



The Chicago and New York City files also have the following two columns:
<ul>

<li>Gender</li>

<li>Birth Year</li>
</ul>

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them (Chicago, New York City, Washington). These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward.

<b>Statistics Computed</b>

You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

<b>#1 Popular times of travel</b> (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day


<b>#2 Popular stations and trip</b>

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

<b>#3 Trip duration</b>

total travel time
average travel time

<b>#4 User info</b>

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)


<b>The Files</b>

To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided in a bikeshare.py file, and you will do your scripting in there also. You will need the three city dataset files too:

chicago.csv
new_york_city.csv
washington.csv
