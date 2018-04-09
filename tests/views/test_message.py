import json


def test_user(app, app_client, db_tables, db):
    c = app_client

    r = c.get('/messages')
    r.json = json.loads(r.data)
    assert r.json['status'] == 1
    assert r.json['data']
