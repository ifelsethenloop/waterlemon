# flask_web/app.py
# Template base flask web app

from flask import Flask
app = Flask(__name__) # create an instance in python

@app.route('/') # route called by user

def hello_world(): # function called by '/' route
    return 'Hey, we have Flask in a container!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
