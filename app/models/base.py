from datetime import datetime
from app.extensions import db

class BaseModel(db.Model):
    """Base model class that includes common columns and methods"""
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 