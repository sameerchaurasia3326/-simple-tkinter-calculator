from flask import Flask

# Create the Flask web app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello():
    return "Hello, World! Your Python app is run."

# This allows the app to be run by a production server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
