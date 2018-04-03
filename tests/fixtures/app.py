# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='session')
def app():
    from alloy.app import app
    return app


@pytest.fixture(scope='session')
def db(app):
    from alloy.app import db
    return db


@pytest.fixture(scope='session')
def db_tables(db):
    # Create tables.
    from alloy.models import Base
    for table in Base.metadata.sorted_tables:
        sql = 'DROP TABLE IF EXISTS {};'.format(table.name)
        db.session().execute(sql)
        db.session().commit()
    with open("sql/schema.sql") as f:
        sql = f.read()
        db.session().execute(sql)
        db.session().commit()
    yield
    # Drop tables.
    for table in Base.metadata.sorted_tables:
        sql = 'DROP TABLE {};'.format(table.name)
        db.session().execute(sql)
        db.session().commit()


@pytest.fixture(scope='function')
def app_client(app):
    return app.test_client()


@pytest.fixture(scope='function')
def Todo(db):
    db.create_all()
    yield Todo
    db.drop_all()
