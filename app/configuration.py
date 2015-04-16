class BaseConfig:
    """
    Base config class
    """
    SECRET_KEY = ""
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = "my value"


class ProductionConfig(BaseConfig):
    """
    Production specific config
    """
    SECRET_KEY = "Need to read key from someplace secret"
    DEBUG = False


class StagingConfig(BaseConfig):
    """
    Staging specific config
    """
    pass


class DevelopmentConfig(BaseConfig):
    """
    Development environment specific
    """
    TESTING = True
