from flask import Flask, render_template, send_file
from ffmpeg_streaming import Formats, input

app = Flask(__name__, static_folder='lives', static_url_path='/videos')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stream/<name>")
def video(name):
    print(f"lives/{name}")
    return send_file(f"lives/{name}")

if __name__ == "__main__":
    app.run(debug=True)