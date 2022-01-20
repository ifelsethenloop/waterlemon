# flask_web/app.py
# Template base flask web app

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a container!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
