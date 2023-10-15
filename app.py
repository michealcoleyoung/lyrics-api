from azapi import AZlyrics
from flask import Flask, render_template, request
import pprint
import time

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    api = AZlyrics("google")
    if request.method == 'POST':

        # user song and artist search
        api.artist = request.form['search_artist']
        api.title = request.form['search_lyrics']


        if api.artist == '' and api.title == '':
            print("========= ARTIST FIELD AND SONG FIELD ARE BLANK =========")
            error_message = "Please enter either an artist or song name"
            return render_template('index.html', error_message=error_message)
        elif api.artist and api.title == '':
            print("========= ARTIST FIELD IS NOT BLANK AND SONG FIELD IS BLANK  =========")
            songs = api.getSongs()
            print(songs)
            return render_template('index.html',songs=songs)
        elif api.artist == '' and api.title:
            print("========= ARTIST FIELD IS BLANK AND SONG FIELD IS NOT BLANK  =========")
            lyrics = api.getLyrics()
            formatted_lyrics = lyrics.replace('\n', '<br>')
            return render_template('index.html',song=api.title, lyrics=formatted_lyrics)
        else:
            print("========= ARTIST FIELD SONG FIELDS ARE NOT BLANK  =========")
            lyrics = api.getLyrics()
            formatted_lyrics = lyrics.replace('\n', '<br>')
            return render_template('index.html',song=api.title, lyrics=formatted_lyrics)     


if __name__ == "__main__":
    app.run(debug=True)