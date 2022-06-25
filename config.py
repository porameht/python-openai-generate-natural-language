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
