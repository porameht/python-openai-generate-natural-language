##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
