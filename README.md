# Udacity-Full-Stack-Nanodegree---Logs-Analysis

## Description

The task for this project was to write a python program that acts as a reporting tool. Given three queries, the program returns the results for those queries in plain text. This program uses the psycopg2 module to connect to the database.

## Setup

1. Make sure you have Python2.7, Vagrant and VirtualBox installed on your computer. (Download links are provided below.)

Python2.7 Download

VirtualBox Download

Vagrant Download

2. Download the data for the newsdata database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

3. After unzipping the file, place the newsdata.sql file into your vagrant directory.

4. Make sure you cd into the vagrant directory in your console window. Load the data by using the command ```psql -d news -f newsdata.sql```.

5. Connect to the database using the command ```psql -d news```.

6. Creating views:

7. Place the python file (newsdata.py) from this repository into your vagrant directory.

8. Using your console window, run the python program with ```python newsdata.py```.

## Resources

Python2.7

VirtualBox

Vagrant

Newsdata File

