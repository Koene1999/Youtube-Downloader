import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def Youtube_Downloader():
    update = os.system('pip install --upgrade pytubefix')
    print('Done!')
    return f'{update}'

@app.route('/Update')
def Updater():
    update_pip = os.system('python -m pip install --upgrade pip')