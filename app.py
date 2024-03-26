import asyncio
from threading import Thread

from app_pyrtmp import main
from app_flask import app as flask

def runFlask():
    flask.run(debug=True)

def runRtmp():
    asyncio.run(main())

# flaskThread = Thread(target=runFlask, args=[]) # ValueError: signal only works in main thread of the main interpreter
rtmpThread = Thread(target=runRtmp, args=[])

# flaskThread.start()
rtmpThread.start()

runFlask()
# flaskThread.join()
rtmpThread.join()