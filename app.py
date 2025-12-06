import os
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/url')
def url_page():
    os.system('ffmpeg -h')
    return 'Done!'
