from azapi import AZlyrics
from flask import Flask, render_template, request
import pprint
import time

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        api = AZlyrics("google")

        # user song search
        api.title = request.form['search_lyrics']
        # api.artist = request.form['search_artist']

        

        # correct formatting of printed lyrics

        if api.title:
            lyrics = api.getLyrics()
            formatted_lyrics = lyrics.replace('\n', '<br>')
            return render_template('index.html',song=api.title, lyrics=formatted_lyrics)
        elif api.title == '':
            return render_template('index.html')
        else:
            return "<h1>There are no songs by this name</h1>"
        

    return render_template('index.html')

    

if __name__ == "__main__":
    app.run(debug=True)