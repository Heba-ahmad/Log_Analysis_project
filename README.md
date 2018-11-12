#  Log Analysis Project
Log Analysis project is a project provided by [Udacity's Full Stack Web Developer Nanodegree](https://sa.udacity.com/course/full-stack-web-developer-nanodegree--nd004). It is an internal reporting tool that prints out reports (in plain text) based on the data in the database to discover what kind of articles the site's readers like. 

## Getting Started

In this project, you will get practice interacting with a live database both from the terminal and from your code.  It is a Python program using the psycopg2 module to connect to the database. The database contains newspaper articles, and the web server log for the site. The log has a database row for each time a reader loaded a web page.
The code of this tool will answer the following questions about the site's user activity:
1.	**What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top
2.	**Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3.	**On which days did more than 1percent of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

### Prerequisites
You will need to install the following programs to build this tool successfully:
```
•	Python 3.7.1
•	psycopg2
•	pycodestyle
•	Terminal
•	Vagrant
•	VirtualBox
```

### Installing

•	Install [python3](https://www.python.org/downloads/)

•	Install psycopg2 :
open your terminal run the following command:
```
pip install psycopg2
```

•	Install pycodestyle 
open your terminal run the following command:

```
pip3 install pycodestyle
```

•	Install [Git Bash terminal that comes with the Git software]( https://git-scm.com/downloads) For Windows user. Terminal For Mac or Linux user, will do just fine.

•	Install [Vagrant]( https://www.vagrantup.com/downloads.html)
If Vagrant is successfully installed, you will be able to run 
     ```
vagrant –version
     ```
          in your terminal to see the version number.


•	Install [VirtualBox]( https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)


## Setup Project:

**Once you get the above software installed, follow the following instructions:**

1.	Download or clone then unzip the vagrant setup files from [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) or [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
2.	Download [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3.	Unzip the data to get the newsdata.sql file.
4.	Put the newsdata.sql file into the vagrant directory
5.	Download this project: [Log_analysis_Project1](https://github.com/Heba-ahmad/Log_Analysis_project.git)
6.	Upzip as needed and copy all files into the vagrant directory into a folder called Log_Analysis_project


## Launching the Virtual Machine:

1.	Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
```
    $ cd FSND-Virtual-Machine
    $ cd vagrant
    $ vagrant up
  ```
2.	Then Log into this using command:
```
  $ vagrant ssh
```
3.	Change directory to /vagrant then / log-analysis-project and look around with 
```
ls 
cd /vagrant
cd/ log-analysis-project
```
4.	Load the data in local database using the command:
```
  psql -d news -f newsdata.sql
```
5.	Use ```psql -d news ```to connect to database.
6.	Create view tables using the following command :
 ```
CREATE VIEW top_articles_views AS 
SELECT articles.title, COUNT(*) AS views
FROM articles JOIN authors 
ON authors.id = articles.author
JOIN log ON path LIKE concat('/article/%', articles.slug)
GROUP BY articles.title
ORDER BY VIEWs DESC;
```
```
CREATE VIEW total_errors AS SELECT date(time), COUNT(*) AS errors
FROM log WHERE status= '404 NOT FOUND' 
GROUP BY date(time) 
ORDER BY errors;

```
```
CREATE VIEW total_time AS SELECT date(time), COUNT(*) AS totaltime
FROM log 
GROUP BY date(time) 
ORDER BY totaltime;
```
```
CREATE VIEW percentage_errors AS
SELECT total_time.date, 
ROUND((total_errors.errors*100.0/total_time.totaltime), 3)AS percentage
FROM total_time, total_errors
WHERE total_time.date = total_errors.date
ORDER BY total_time.date;
```
7. then Run python loganalysisdb.py

## Run The Project python file:

1. You should already have vagrant up and be connected to it. 
1. If you aren't already, cd into the correct project directory: ``` cd /vagrant/log-analysis-project ```
1. Run ``` python loganalysisdb.py ```

Generating this information will take several seconds, but will now start loading. 

## Expected Output: 
1. The most popular three articles of all time:

      Candidate is jerk, alleges rival - 338647 Views
      Bears love berries, alleges bear - 253801 Views
      Bad things gone, say good people - 170098 Views

2. The most popular article authors of all time:

      Ursula La Multa - 507594 Views
      Rudolf von Treppenwitz - 423457 Views
      Anonymous Contributor - 170098 Views
      Markoff Chaney - 84557 Views

3. Days that have more than 1% of requests lead to errors:

      2016-07-17 - 2.263% Errors


### Coding style tests
pycodestyle (formerly called pep8) - Python style guide checker
This package used to be called pep8 but was renamed to pycodestyle to reduce confusion
A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is most important.

#### Example usage and output

**exp. With error**

```
pycodestyle --first loganalysisdb.py
loganalysisdb.py:56:1: E305 expected 2 blank lines after class or function defin
ition, found 1
 ```
**exp. With no error**
```
C:\Users\InfoTech\Desktop\fsnd-virtual-machine\vagrant\log-analysis-project>pyco
destyle --first loganalysisdb.py

C:\Users\InfoTech\Desktop\fsnd-virtual-machine\vagrant\log-analysis-project>
```

## Deployment

To deploy my app on a live system, I need to use tools like flask and virtualenv. Flask is a micro framework that makes the process of designing a web application simpler. It lets us focus on what the users are requesting and what sort of response to give back. Virtualenv is used to create an isolated environment for our Python project.
And by using Platform as a Service (PaaS), like Google App Engine and Heroku. 
Here are the steps we need to follow to deployment using Heroku: 

•	Check your server code into a new local Git repository.

•	Sign up for a free Heroku account.

•	Download the Heroku command-line interface (CLI).

•	Authenticate the Heroku CLI with your account: heroku login

•	Create configuration files Procfile, requirements.txt, and runtime.txt and check them into your Git repository.

•	Modify your server to listen on a configurable port.

•	Create your Heroku app: heroku create your-app-name

•	Push your code to Heroku with Git: git push heroku master


## Authors

** Heba Ahmad ** - *add project files* - [Heba_Ahmad](https://github.com/Heba-ahmad/log_analysis_project)

## Acknowledgments
* https://github.com/bcko/Ud-FS-LogsAnalysis-Python
* https://github.com/SteveWooding/fsnd-logs-analysis-project/blob/master/logs_analysis_tool.py
* https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492
* [Deploying to a hosting service](https://classroom.udacity.com/nanodegrees/nd004-connect/parts/e8e83eef-dbd4-4a9e-8a21-21c6a7adf71b/modules/2a89d1b1-8ceb-4f42-8d3a-eb91701873e7/lessons/773150bb-8e88-4457-b077-3b8a02018f33/concepts/1d84f620-4d25-45fd-aa10-276498e328ae)
* [Andrew T Baker 5 ways to deploy your Python web app in 2017 PyCon 201](https://youtu.be/vGphzPLemZE)





