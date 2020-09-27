import click
from pequifood.ext.db import db
from pequifood.ext.auth.models import User
from pequifood.ext.site import models 


def init_app(app):
    @app.cli.command()
    def create_db():
        """ Este comando inicializa o db"""
        db.create_all()
        
        
    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """Adiciona um novo Usuario"""
        user = User(email=email, 
                    passwd=passwd, 
                    admin=admin
                    )
        db.session.add(user)
        db.session.commit()
        click.echo(f"Usuario { email } criado com Sucesso")
        
        
    @app.cli.command()
    def listar_usuarios():
        users = User.query.all()
        for user in users:
            click.echo(user)
        
    @app.cli.command()
    def listar_produtos():
        click.echo("Listar Produtos")
    