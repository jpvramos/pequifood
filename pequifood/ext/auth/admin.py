from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from pequifood.ext.auth.models import User 
from pequifood.ext.db import db 
from flask import flash, Markup


def format_user(self, request, user, *args):
    return user.email.upper().split("@")[0]

class UserAdmin(ModelView):
    """Interface admin de user"""
    
    column_formatters = {"email": lambda s, r, u, *a:Markup(f'<b>{u.email.split("@")[0]}</b>')}
    
    column_list =  ["email", "admin"]
    can_edit = False
    can_create = True
    can_delete = True
    column_searchable_list = ["email"]
    column_filters = ["email", 
                    "admin",
                    filters.FilterLike(
                    User.email, 
                    "Dominios email",
                    options=(("gmail", "GMAIL"), ("uol", "UOL"))
                    )]
    
    @action(
        'toggle_admin', 
        'Toggle admin status', 
        'Are you sure?'
    ) 
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
            
        db.session.commit()
        flash(f"{len(users)} Usuarios alterados com Sucesso", "success")
        
        
    @action(
        'send_email',
        'send emails for all users?', 
        'Are yopu sure?'
        
    )
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        flash(f"{len(users)} Usuarios alterados com Sucesso", "success")
        