import datetime

from app import app, db
from sqlalchemy.dialects.mysql import INTEGER, BIGINT, TIMESTAMP
from sqlalchemy.sql.expression import text


class ImageModel(db.Model):
    __bind_key__ = app.config.get('DEFAULT_DATABASE')
    __tablename__ = 'images'
    __table_args__ = {
        'schema': __bind_key__,
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'extend_existing': True
    }

    id = db.Column(
        BIGINT(20, unsigned=True),
        primary_key=True,
        index=True
    )
    key = db.Column(
        db.String(32),
        nullable=False
    )
    file_format = db.Column(
        db.String(32),
        nullable=False
    )
    size = db.Column(
        INTEGER(unsigned=True)
    )
    created_date = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )
