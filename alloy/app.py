# -*- coding: utf-8 -*-
from psycogreen.gevent import patch_psycopg
patch_psycopg()  # noqa

import gevent.monkey
gevent.monkey.patch_all()   # noqa

import threading
from flask import Flask
from flask import _app_ctx_stack
from flask_sqlalchemy import SQLAlchemy


def scopefunc():
    if _app_ctx_stack.top is None:
        return threading.current_thread().ident
    else:
        return _app_ctx_stack.__ident_func__()


db = SQLAlchemy(session_options={'scopefunc': scopefunc})
app = Flask(__name__)


def create_app(config_name):
    from .config import config
    from . import models
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    db.app = app

    models.Base.db = db
    models.Base.query = db.session.query_property()

    return app


from .views import *  # noqa
