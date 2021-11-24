#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)

# Monkey-patch app.get/post/etc. for Flask <2 compatibility
if not hasattr(flask.Flask, 'post'):

    def _add_flask_method(name):
        def meth(self, rule: str, **options):
            return self.route(rule, methods=[name.upper()], **options)

        setattr(flask.Flask, name, meth)

    for method in ('get', 'post', 'put', 'delete', 'patch'):
        _add_flask_method(method)

from . import logging  # noqa: F401, E402
from . import routes  # noqa: F401, E402
from . import cleanup  # noqa: F401, E402
from . import db  # noqa: F401, E402
from . import onion_req  # noqa: F401, E402
