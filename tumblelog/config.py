class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS= {'DB':"my_tumble_log"}
    SECRET_KEY = "KSFSDFSDFSGKSDJFGKDFGJDFGJDFKGDFJGDFKGJDFKGJ"

class ProductionConfig(Config):
    MONGOLAB_URI="mongodb://woosungchu:cws2cws;@ds017514.mlab.com:17514/heroku_fj7fqx00"
    $PORT = 5000

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True