# -*- coding: utf-8 -*-
from flask import jsonify
from flask.globals import request

from ..app import app, db

from ..models import User


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).scalar()
    return jsonify({'id': user.id, 'nickname': user.nickname})


@app.route('/user', methods=['POST'])
def create_user():
    user = User(**request.get_json())
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id})
