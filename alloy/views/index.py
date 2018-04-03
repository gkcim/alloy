# -*- coding: utf-8 -*-


from ..app import app


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'Welcome to Alloy!'
