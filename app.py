from flask import Flask
import os
app = Flask(__name__)

@app.route('/')

def home():
    return'Hello! Welcome to my Web Page of G23AI2061'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =5000)