import os
from flask import Flask, render_template, request
app = Flask(__name__)

#tot en met & bij title
#video toevoegen
#playlist toevoegen
#error handling

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/url')
def url_page():
    os.system('pip install --upgrade pytubefix')
    os.system('rm Downloads/*')
    return render_template('url.html')

@app.route('/download', methods=['POST'])
def download():
    from pytubefix import helpers
    from pytubefix import YouTube
    url = request.form.get('url')
    media = request.form.get('media')
    filetype = request.form.get('filetype')
    youtube = YouTube(url)
    title = helpers.safe_filename(youtube.title)
    if media == 'audio':
        audio = youtube.streams.filter(only_audio=True).order_by("abr").last()
        audio.download("","Audio")
        os.system(f'ffmpeg -i Audio "Downloads/{title}.{filetype}"')
        os.system('rm Audio')
    print(os.system('ls Downloads'))
    return 'Download ready'