from flask import Flask, render_template, url_for
import requests
from lyricsgenius import Genius
import config
import re

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    genius = Genius(config.API_KEY)
    artist_name = "Zero 7"
    song_name = "Warm Sound"
    artist = genius.search_artist(f"{artist_name}", max_songs=1, sort="title")
    song = genius.search_song(f"{song_name}", artist.name)
    print(artist.save_lyrics)

    def clean_lyrics(lyrics):
        # Use regular expression to remove everything before and after "Lyrics"
        lyrics = re.sub(r".*Lyrics", "", lyrics)
        # Use regular expression to remove everything after "Embed"
        lyrics = re.sub(r"Embed*", "", lyrics)
        # Strip any leading or trailing whitespace
        return lyrics.strip()

    image = song.header_image_thumbnail_url

    print(clean_lyrics(song.lyrics))

    if requests.method == 'POST':
        search_query = request.form['search_query']
        

    return render_template('index.html', artist=song.artist, title=song.title, lyrics=clean_lyrics(song.lyrics), image=image)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')