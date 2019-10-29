# Log Analysis

This project is a collection of queries to analysis the database and produce reports.
It's answer three questions and they are:

* What are the most popular three articles?
* Who are the most popular article authors?
* On which days did more than 1% of requests lead to errors?

## Technologies Uesd
* Vagrant
* Virtualbox
* Python
* SQL

## Setup
* Ensure that Python, the python package psycopg2, Vagrant, and VirtualBox are installed.
* Download the [fullstack-nanodegree-vm](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).
* Download the [SQL database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip, and save `newsdata.sql` in the vagrant directory.
* Navigate to the vagrant folder in the terminal and enter `vagrant up` to bring the server online, followed by `vagrant ssh` to log in.
* To run the SQL queries directly, navigate to the vagrant directory with `cd /vagrant`, then enter `psql -d news -f newsdata.sql` to connect to and run the project database.
* To execute the program, run `python reporting_tool.py`.

## The views used in this project

* The errors is used to have the error logs and it's count per day, created as following:
`create or replace view errors as select date(time), count(time) from log where status<>'200 OK' group by date(time) order by date(time);`
* The requests is used to have all requests logs and it's count per day, created as following:
`create or replace view requests as select date(time), count(time) as requests from log group by date(time);`

### The project consist of 3 main functions as following:
* The get_top_articles to get the top 3 articles in number of views.
* The get_top_authors to get the authors ordered by the number of the views of their articles.
* The get_requests_fail_days to get the days on which the requests lead to more than 1% errors.
