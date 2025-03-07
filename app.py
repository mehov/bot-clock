import os
from src.Http import http as app
# If Azure is running something like gunicorn -b 0.0.0.0:8000 app:app, then it expects an app variable in app.py.


if __name__ == '__main__':
    app.run()
