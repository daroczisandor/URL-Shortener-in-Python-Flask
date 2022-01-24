from flask import Flask, request, jsonify

# creating Flask app
app = Flask(__name__)

# Defining what will happen on the main route
@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=7777, debug=True)
