import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def Youtube_Downloader():
    update1 = os.system('python -m pip install --upgrade pip')
    update2 = os.system('pip install --upgrade pytubefix')
    print('Done!')
    return f'{update1}, {update2}'