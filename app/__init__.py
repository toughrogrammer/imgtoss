import click
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


#
# import model and create models
#
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from app.models import *


#
# import route functinos
#
from app.routes import *


# cli
@app.cli.command()
def initdb():
    click.echo('create all models')
    db.create_all(bind=[
        app.config.get('DEFAULT_DATABASE')
    ])
