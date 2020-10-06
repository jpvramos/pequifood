import click
from pequifood.ext.db import db, models


def init_app(app):
    @app.cli.command()
    def create_db():
        """ Este comando inicializa o db"""
        db.create_all()
        
    
    @app.cli.command()
    def list_products():
        """ List of all products"""
        click.echo("Listar Produtos")
    