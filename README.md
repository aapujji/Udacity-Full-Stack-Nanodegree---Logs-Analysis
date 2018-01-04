# Udacity-Full-Stack-Nanodegree---Logs-Analysis

## Description

The task for this project was to write a python program that acts as a reporting tool. Given three queries, the program returns the results for those queries in plain text. This program uses the psycopg2 module to connect to the database.

## Setup

1. Make sure you have Python2.7, Vagrant and VirtualBox installed on your computer. (Download links are provided below.)

    [Python2.7 Download](https://www.python.org/downloads/)

    [VirtualBox Download (5.1.30)](https://www.virtualbox.org/wiki/Downloads)

    [Vagrant Download (1.8.5)](https://releases.hashicorp.com/vagrant/?_ga=2.146818743.1445943320.1515078265-241047305.1515078265)

2. [Downlaod the vm]() (if you don't already have one)

3. Download the data for the newsdata database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

4. After unzipping the file, place the newsdata.sql file into your vagrant directory.

5. Make sure you cd into the vagrant directory in your console window. Load the data by using the command ```psql -d news -f newsdata.sql```.

6. Connect to the database using the command ```psql -d news```.

7. Create views:

    a. Create view for ```errors_table```:

        create view errors_table as select date(time) as date, count(*) as total, sum(case when status != '200 OK' then 1 else 0 end) as err from log group by date(time) order by err;

    b. Create view for ```err_perc```:
    
        ```create view err_perc as select date, cast(err as float)/cast(total as float)*100 as perc from errors_table group by date, perc order by perc;```
        
8. Place the python file (newsdata.py) from this repository into your vagrant directory.

9. In your console window, run the python program using ```python newsdata.py```.
