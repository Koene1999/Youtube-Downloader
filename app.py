import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Youtube Downloader'

@app.route('/download')
def download():
    os.system('pip install --upgrade pytubefix')
    return 'Download'