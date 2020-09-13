from flask import Flask
from pequifood.ext  import site
from pequifood.ext import toolbar
from pequifood.ext import config


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    
    
    return app