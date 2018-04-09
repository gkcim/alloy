# -*- coding: utf-8 -*-
import json
import os

from ..app import app
from flask import jsonify


@app.route('/messages', methods=['GET'])
def get_messages():
    fp = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../files/messages.json'))
    return jsonify(json.load(open(fp)))
