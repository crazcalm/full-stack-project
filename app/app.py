from flask.ext.script import Manager
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

manager = Manager(app)
app.config['DEBUG'] = True  # Ensure debugger will load


if __name__ == "__main__":
    manager.run()
