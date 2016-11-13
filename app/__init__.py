import click
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


#
# aws boto3
#
import boto3

boto3_session = boto3.session.Session(
	aws_access_key_id=app.config.get('AWS_ACCESS_KEY_ID'),
	aws_secret_access_key=app.config.get('AWS_SECRET_ACCESS_KEY'),
	region_name='ap-northeast-2')


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
