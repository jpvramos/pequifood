from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from pequifood.ext.db import db
from pequifood.ext.db.models import Category


admin = Admin()

def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "PequiFood")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE","bootstrap4")
    admin.init_app(app)
    
    admin.add_view(ModelView(Category, db.session))
    