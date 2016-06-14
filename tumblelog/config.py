class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS= {'DB':"my_tumble_log"}
    SECRET_KEY = "KSFSDFSDFSGKSDJFGKDFGJDFGJDFKGDFJGDFKGJDFKGJ"

#class ProductionConfig(Config):

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True