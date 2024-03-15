from flask import Flask
from blueprint import trap
import random
# creates and defines an app using flask
def make_app():
    app = Flask(__name__)
    app.register_blueprint(trap)
    return app
# sets up the website
if __name__ == '__main__':
    app = make_app()
    app.run(host='localhost', port=8083, debug=True)