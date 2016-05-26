import os
from flask import Flask

app = (Flask__name__)

@app.route('/')
def hello():
    return 'Hello Worl'

if __name__== '__main__':
    #bind to port if defined, otherwise default
    port = int(os.environ.get('PORT', 5000))
    app.runhost=('0.0.0.0', port=port)
