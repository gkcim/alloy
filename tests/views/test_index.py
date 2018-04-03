# -*- coding: utf-8 -*-


def test_index(app_client):
    r = app_client.get('/')
    assert r.status_code == 200
    assert r.data.decode() == 'Welcome to Alloy!'
