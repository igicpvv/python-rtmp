import asyncio
from example.demo_ffmpeg import main as hlsServer

from flask import Flask

from threading import Thread

####################################
# RTMP
def startRTMP():
    asyncio.run(hlsServer())

threadRtmp = Thread(target=startRTMP, args=[])
####################################

####################################
# FLASK
app = Flask(__name__, static_folder='example/lives', static_url_path='/videos')


####################################





threadRtmp.start()
app.run(debug=True)

