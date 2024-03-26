from flask import Flask, render_template, send_file

app = Flask(__name__, static_folder='lives', static_url_path='/stream')

@app.route("/")
def index():
    return render_template('index.html')


# @app.route("/stream/<name>")
# def video(name):
#     print(f"lives/{name}")
#     return send_file(f"lives/{name}")