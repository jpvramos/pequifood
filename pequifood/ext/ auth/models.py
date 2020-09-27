from pequifood.ext.db import db
 

class User(db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.Unicode, unique=True)
    passwd = db.Column("passwd", db.Unicode)
    admin = db.Column("admin", db.Boolean)
    
    def __repr__(self):
        return f"Email: {self.email} \nsenha: {self.passwd} \nadministrador: {'VERDADEIRO' if self.admin > 0 else 'FALSO'}" 