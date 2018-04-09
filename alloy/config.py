import os
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))


class Config(object):
    SERVICE_VERSION = ''
    JSONIFY_MIMETYPE = 'application/json; charset=utf-8'

    SQLALCHEMY_POOL_SIZE = 80
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_POOL_RECYCLE = 60*60
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True

    DATABASE_QUERY_TIMEOUT = 0.001

    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')

    CACHE_TYPE = 'redis'
    CACHE_REDIS_URL = 'redis://{}/0'.format(REDIS_HOST)
    CACHE_KEY_PREFIX = 'api4flask_cache_'
    CACHE_DEFAULT_TIMEOUT = 300

    SESSION_REDIS_URL = 'redis://{}/1'.format(REDIS_HOST)

    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_BINDS = {}
    TEMPLATES_AUTO_RELOAD = True
    EXPLAIN_TEMPLATE_LOADING = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = False
    SERVICE_VERSION = 'dev'

    SQLALCHEMY_RECORD_QUERIES = True
    DATABASE_QUERY_TIMEOUT = 0.001

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://localhost:5432/dev_alloy'


class TestingConfig(Config):
    TESTING = True
    SERVICE_VERSION = 'testing'

    SQLALCHEMY_DATABASE_URI = \
        'postgresql+psycopg2://{}:5432/test_alloy'.format(Config.DB_HOST)


class ProductionConfig(Config):
    SERVICE_VERSION = 'production'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
