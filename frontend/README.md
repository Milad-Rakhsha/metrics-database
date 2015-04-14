# ChronoTest_Frontend
Website for Tests in Chrono.

Setup:

Start a virtualenv for the frontend. This should preferably be inside the frontend folder.
```
virtualenv MetricsFrontend
source MetricsFrontend/bin/activate
```

Install the required packages
```
pip install -r requirements.txt
```

In order to communicate with the API and make requests you need to have one of the registered users login. If you have that information create a json file that looks like this:

```
{
username: "SAMPLE USERNAME"
pw: "THE PASSWORD"
}
```

Then, change the PATH variable in config_example.py to the path to the json file that contains user information. 

Finally, change the BACKEND variable in config_example.py to the url of the api:

```
BACKEND_URL = "URL to backend API. In my case it would be http://localhost:5000/chrono_test/api/"
```

Once all of this is done rename config_example.py to config.py 

To start running the website:
If virtual environment is running run the command
```
python run.py
```
If virtual environment is NOT running run the command:
```
chronoTestFrontend/bin/python run.py
```

