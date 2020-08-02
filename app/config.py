import os
from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    """App configuration variables."""

    # app secret key
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    """Allow debug to restart after changes."""

    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Testing the application."""

    DEBUG = True
    TESTING = True


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True


class ReleaseConfig(Config):
    """Releasing app configurations."""

    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    """Production configurations."""

    pass


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}