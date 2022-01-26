## URL shortener in Python

This is an URL shortener service written using Flask / Python.

### Project details:

- Language: Python
- Framework: Flask
- IDE: PyCharm

### Endpoints:

I. /encode/

- Given a long URL argument as e.g. "http://127.0.0.1:7777/encode?url=https://wikipedia.org", it returns a JSON containing a short URL of the form "http://127.0.0.1:7777/6M0qc" corresponding to the long link provided, or an error message if the conversion could not be performed.


II. /decode/

- Given a short URL argument as e.g. "http://127.0.0.1:7777/decode?url=http://127.0.0.1:7777/6M0qc", it returns a JSON containing the corresponding decoded long URL, if it exists, or an error message otherwise.


#### Notes:
Using port 7777 instead of the default 5000.