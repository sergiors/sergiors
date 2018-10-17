# -*- coding: utf-8 -*-


from functools import update_wrapper
from datetime import timedelta
from flask import current_app
from flask import make_response
from flask import request


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):

    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))

    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)

    if not isinstance(origin, str):
        origin = ', '.join(origin)

    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        default_response = current_app.make_default_options_response()
        return default_response.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                res = current_app.make_default_options_response()
            else:
                res = make_response(f(*args, **kwargs))

            h = res.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)

            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers

            return res

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator
