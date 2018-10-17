# -*- coding: utf-8 -*-

import json

from flask import Flask
from flask import Response
from flask import request
from sketchengine import concordance
from crossdomain import crossdomain

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello() -> Response:
    return Response(None)


@app.route('/examples', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def examples() -> Response:
    q = request.args.get('q')

    if q is None:
        return Response(json.dumps([]), mimetype='application/json')

    return Response(
        response=json.dumps(concordance(query=q)),
        mimetype='application/json')