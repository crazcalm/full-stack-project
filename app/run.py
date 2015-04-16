from flask.ext.script import Manager
from app import app
#from configuration import ProductionConfig
#from configuration import StagingConfig
from configuration import DevelopmentConfig


app.config.from_object(DevelopmentConfig)
print(app.config)
manager = Manager(app)
manager.run()
