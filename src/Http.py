import logging
import os
from wsgiref.simple_server import make_server
from datetime import datetime
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify)

http = Flask(__name__)


@http.route('/')
def index():
    print('Request for index page received')
    return jsonify(
        hello='world',
        now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )


@http.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')

    if name:
        print('Request for hello page received with name=%s' % name)
        return render_template('hello.html', name=name)
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))
