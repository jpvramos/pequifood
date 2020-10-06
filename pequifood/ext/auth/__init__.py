from pequifood.ext.auth import models
from pequifood.ext.auth.commands import list_users, add_user

from pequifood.ext.admin import admin as main_admin
from pequifood.ext.auth.admin import UserAdmin
from pequifood.ext.db import db 
from pequifood.ext.auth.models import User


def init_app(app):
    # TODO Flask-SimpleLogin JWT
    ... 
    app.cli.command()(list_users)
    app.cli.command()(add_user)
    
    main_admin.add_view(UserAdmin(User, db.session))