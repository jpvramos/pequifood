from flask import Flask
from pequifood.ext  import site
from pequifood.ext import toolbar
from pequifood.ext import config
from pequifood.ext import db
from pequifood.ext import cli
from pequifood.ext import auth
from pequifood.ext import migrate
from pequifood.ext import admin


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    
    
    return app