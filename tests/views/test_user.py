import json

from flask.testing import FlaskClient
from flask.wrappers import Response

from alloy.models.user import User


def test_user(app, app_client, db_tables, db):
    data = dict(nickname='nickname',
                realname='realname',
                password='password',
                email='email',
                phone='phone')

    c = app_client
    assert isinstance(c, FlaskClient)
    r = c.post('/user',
               content_type='application/json',
               data=json.dumps(data))
    assert isinstance(r, Response)
    r.json = json.loads(r.data)
    user = db.session.query(User).limit(1).scalar()
    assert user.id > 0
    assert user.nickname == 'nickname'

    r = c.get('/user/{}'.format(user.id))
    r.json = json.loads(r.data)
    assert r.json['id'] == user.id
    assert r.json['nickname'] == user.nickname
