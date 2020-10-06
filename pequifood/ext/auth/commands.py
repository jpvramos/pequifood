import click

from pequifood.ext.db import db
from pequifood.ext.auth.models import User


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



def list_users():
    users = User.query.all()
    for user in users:
        click.echo(user)