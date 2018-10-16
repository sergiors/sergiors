# -*- coding: utf-8 -*-

import json

from flask import Flask
from flask import Response
from sketchengine import concordance

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello() -> Response:
    return Response(None)


@app.route('/examples/<string:word>', methods=['GET'])
def examples(word: str) -> Response:
    return Response(
        response=json.dumps(concordance(word)),
        mimetype='application/json')