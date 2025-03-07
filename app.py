import os
import threading
from src.Http import http as app
from src.Bot import Bot
# If Azure is running something like gunicorn -b 0.0.0.0:8000 app:app, then it expects an app variable in app.py.


# app.run() # no need for this as Azure has a separate launcher
