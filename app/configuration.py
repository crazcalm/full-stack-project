import secret
"""
This file is dedicated to the classes used to configure the application.
"""


class BaseConfig:
    """
    Base configuration.
    The parent of all the other configuration classes.
    """
    SECRET_KEY = ""
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = "my value"


class ProductionConfig(BaseConfig):
    """
    Production specific config
    """
    SECRET_KEY = secret.SECRET
    DEBUG = False


class StagingConfig(BaseConfig):
    """
    Staging specific config
    """
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """
    Development environment specific
    """
    TESTING = True
