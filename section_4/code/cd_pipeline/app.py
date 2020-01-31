from flask import Flask, render_template
import random

app = Flask(__name__)

# list of pug images
images = [ "https://media.giphy.com/media/qJQ0p9ZugSEW4/giphy.gif", 
          "https://media.giphy.com/media/FbyqoWvEHmV9K/giphy.gif", 
          "https://media.giphy.com/media/xUOxfbuK9qc61NGiaI/giphy.gif", 
          "https://media.giphy.com/media/DTgZq3XBUwQgM/giphy.gif", 
          "https://media.giphy.com/media/eIi98sRBy2iRO/giphy.gif", 
          "https://media.giphy.com/media/26gsuJYcHXm0oARQQ/giphy.gif", 
          "https://media.giphy.com/media/xAFPuHVjmsBmU/giphy.gif", 
          "https://media.giphy.com/media/dTJd5ygpxkzWo/giphy.gif", 
          "https://media.giphy.com/media/3oKIPsx2VAYAgEHC12/giphy.gif", 
          "https://media.giphy.com/media/3lxD1O74siiz5FvrJs/giphy.gif" ]


@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
