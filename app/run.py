from flask.ext.script import Manager
from app import app
from configuration import ProductionConfig
from configuration import StagingConfig
from configuration import DevelopmentConfig


def set_config(name):
    """
    A function to select a config option.
    """
    if name == "dev":
        app.config.from_object(DevelopmentConfig)
    elif name == "stage":
        app.config.from_object(StagingConfig)
    elif name == "prod":
        app.config.from_object(ProductionConfig)
    else:
        print("Not a valid config option!")
        return None
    return app


if __name__ == "__main__":
    configured_app = set_config("stage")
    print(configured_app.config)
#manager = Manager(app)
#manager.run()
