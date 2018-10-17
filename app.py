# -*- coding: utf-8 -*-

import json

from flask import Flask
from flask import Response
from flask import request
from sketchengine import concordance

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello() -> Response:
    return Response(None)


@app.route('/examples', methods=['GET'])
def examples() -> Response:
    q = request.args.get('q')

    if q is None:
        return Response(json.dumps([]), mimetype='application/json')

    return Response(
        response=json.dumps(concordance(query=q)),
        mimetype='application/json')