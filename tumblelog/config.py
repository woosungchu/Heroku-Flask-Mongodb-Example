from mongoengine import connect

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "KSFSDFSDFSGKSDJFGKDFGJDFGJDFKGDFJGDFKGJDFKGJ"
    connect(
        'heroku_fj7fqx00',
        host='mongodb://admin:admin@@ds017514.mlab.com:17514/heroku_fj7fqx00',
        port=17514,
        username='admin',
        password='admin',
    )

class ProductionConfig(Config):
#    MONGOLAB_URI="mongodb://woosungchu:cws2cws;@ds017514.mlab.com:17514/heroku_fj7fqx00"
#    MONGODB_SETTINGS = {
#        'db':'my_tumble_log',
#        'host':'ds017514.mlab.com/heroku_fj7fqx00',
#        'port':17514,
#    }
    pass

class DevelopmentConfig(Config):
    DEBUG = True
#    MONGODB_SETTINGS= {'DB':"my_tumble_log"}

class TestingConfig(Config):
    TESTING = True