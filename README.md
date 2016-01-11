# metrics-database
Database for metrics.

Setup:

Clone the repository
```
git clone https://github.com/uwsbel/metrics-database.git
```

In order to setup the whole metrics-database project, follow the README instructions that are in each of the folders (parser, frontend and backend).

## Description
This project was developed to record output metrics (mostly performance) of the tests that are run on the open source multi-physics engine, <a href="http://github.com/" target="_blank">Chrono</a>, and be able to query these metrics and display on a web application. In order to meet this goal I developed five pieces of code that together fully automated the process of tracking these metrics, and a sixth component that will hopefully be implemented in the future. 
                              
**1. BaseTest:** First I developed a BaseTest class from which all tests that wish to report metrics are derived from. This allowed the test developers to easily report the metrics by just calling a simple function called addMetric(...). The class would then output the metrics in a JSON format.

**2. Parser:** The second part of the program was the parser. Whenever a push is made to Chrono there is an automated build system (buildbot based) that runs a bunch of tests, some of which are derived from BaseTest. After all the tests are ran a lot of JSON files have been generated, and builbot calls a parsing script which parses each file and adds them to a PostgreSQL database through an API call.

**3. Metrics Database API:** Any kind of request made to the relational database had to be done through a Flask-based API. This allowed easily handle things like reading and writing to the database, and authentication.

**4. Database:** A PostgreSQL database was used. The database was created and updated using a python package called SQLAlchemy.

**5. Frontend:** The frontend allows Chrono developers to visualize the time evolution of the metrics. This is interesting for performance metrics since you can see how certain parts of Chrono improve (or get worse) in performance as modifications are made. But it can also be used to monitor that the accuracy of certain benchmark simulations stays over a threshold.

**6. Notification System (Not implemented):**  A notification system will hopefully be implemented in the future. The aim of this feature is to notify Chrono users of significant performance decrease after a push is made.
