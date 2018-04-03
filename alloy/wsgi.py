# -*- coding: utf-8 -*-
from gunicorn.app.wsgiapp import WSGIApplication
import gunicorn.util

from .env import env


class AlloyWSGIApp(WSGIApplication):
    def init(self, parser, opts, args):
        self.app_uri = env.app_uri
        args = [self.app_uri]
        super(AlloyWSGIApp, self).init(parser, opts, args)

    def load_wsgiapp(self):
        self.chdir()
        return gunicorn.util.import_app(self.app_uri)

    def run(self):
        super(AlloyWSGIApp, self).run()


def run_app():
    AlloyWSGIApp().run()
