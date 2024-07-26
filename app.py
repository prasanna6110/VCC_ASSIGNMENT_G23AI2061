from flask import Flask
import os
app = Flask(__name__)

@app.route('/')

def home():
    return'<h1>Hello! Welcome to my Web Page of G23AI2061'

app.run()