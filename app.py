from azapi import AZlyrics
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        api = AZlyrics("google")

        # We are Searching for Meghan's song "All about that bass"
        api.title = request.form['search_query']

        lyrics = api.getLyrics()

        formatted_lyrics = lyrics.replace('\n\n', '<p>').replace('\n', '<br>')

        # correct formatting of printed lyrics
        print(lyrics)

        if api.title:
            return render_template('index.html',song=api.title, lyrics=formatted_lyrics)
        else:
            return "<h1>There are no songs by this name</h1>"
    

    return render_template('index.html')

    

if __name__ == "__main__":
    app.run(debug=True)