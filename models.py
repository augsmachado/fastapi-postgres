import datetime as _dt
import sqlalchemy as _sql

import database as _database

class Contact(_database.Base):
    __tablename__ = "contacts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    first_name = _sql.Column(_sql.String, index=True)
    last_name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    phone_number = _sql.Column(_sql.String,unique=True, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
