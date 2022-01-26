## URL shortener in Python

This is an URL shortener service written using Flask / Python.

### Project details:

- Language: Python
- Framework: Flask
- IDE: PyCharm
- Created on Windows


### Setup

The setup instructions are for Windows OS.

1. Navigate to the directory of the downloaded project
2. Make sure Python is installed (version >= 3.7.4)
3. Open command line from the directory, and run the following commands:
- pip install virtualenv
- python -m virtualenv ./
- pip install -r requirements.txt
- python app.py

Then, open a browser of your choice and go to http://127.0.0.1:7777/.



### File structure

- templates
	- home.html
- app.py
- IDEAS.md
- README.md
- requirements.txt
- TASK_OBJECTIVES.md
- url_shortener.py
- utils.py



### Endpoints:

I. /encode/

- Given a long URL argument as e.g. "http://127.0.0.1:7777/encode?url=https://wikipedia.org", it returns a JSON containing a short URL of the form "http://127.0.0.1:7777/6M0qc" corresponding to the long link provided, or an error message if the conversion could not be performed.


II. /decode/

- Given a short URL argument as e.g. "http://127.0.0.1:7777/decode?url=http://127.0.0.1:7777/6M0qc", it returns a JSON containing the corresponding decoded long URL, if it exists, or an error message otherwise.


III. /redirect/

- As a plus, I also integrated a redirect endpoint into the service. This reads in a short_url as e.g. "http://127.0.0.1:7777/redirect?url=http://127.0.0.1:7777/6M0qc", then, similarly to the decode endpoint, it finds the corresponding long_url if has already been encoded. Then instead of just returning it, the endpoint will redirect the page to the given long_url.



### Algorithm for generating the short_url's

The generator algorithms simply generates a sequence of random characters (lowercase letters + uppercase letters + numbers) with length specified by the num_chars variable, and then creates a string via concatenating the base_url with the encoding. This string will be stored as the encoded URL in two dictionaries (to ensure an average lookup time of O(1))



### Testing





#### Notes:

- Keep in mind that the Flask app is using port 7777 instead of the default 5000