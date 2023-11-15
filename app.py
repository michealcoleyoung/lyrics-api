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

        # ARTIST FIELD AND SONG FIELD ARE BLANK
        if api.artist == '' and api.title == '':
            error_message = "Please enter either an artist or song name"
            return render_template('index.html', error_message=error_message)
        
        # ARTIST FIELD IS NOT BLANK AND SONG FIELD IS BLANK
        elif api.artist and api.title == '':
            songs = api.getSongs()
            print(songs)
            error_message = "We cannot find an artist by that name"
            return render_template('index.html',songs=songs, error_message=error_message)
        
        # ARTIST FIELD IS BLANK AND SONG FIELD IS NOT BLANK
        elif api.artist == '' and api.title:
            lyrics = api.getLyrics()
            if isinstance(lyrics, str):
                formatted_lyrics = lyrics.replace('\n', '<br>')
                return render_template('index.html',song=api.title, lyrics=formatted_lyrics)
            else:
                error_message = "An error occurred while retrieving lyrics. Please try again."
                return render_template('index.html', error_message=error_message)
        
        # ARTIST FIELD SONG FIELDS ARE NOT BLANK
        else:
            lyrics = api.getLyrics()
            if isinstance(lyrics, str):
                formatted_lyrics = lyrics.replace('\n', '<br>')
                return render_template('index.html',song=api.title, lyrics=formatted_lyrics)
            else:
                error_message = "An error occurred while retrieving lyrics. Please try again."
                return render_template('index.html', error_message=error_message)
    else:
        return render_template("index.html")
    

@app.route("/get_lyrics", methods=['GET'])
def get_lyrics():
    artist = request.args.get('artist')
    title = request.args.get('title')

    api = AZlyrics("google")
    api.artist = artist
    api.title = title

    lyrics = api.getLyrics()
    formatted_lyrics = lyrics.replace('\n', '<br>')

    return render_template('index.html', song=title, lyrics=formatted_lyrics)

if __name__ == "__main__":
    app.run(debug=True)