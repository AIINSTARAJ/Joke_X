from flask_sqlalchemy import SQLAlchemy  # type: ignore

from sqlalchemy.sql import func # type: ignore

from werkzeug.security import *

import time

import sys 

sys.path.insert(0,'../../')

db = SQLAlchemy()

class user(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    user_ = db.Column(db.String(12),nullable = False)
    pwd_ = db.Column(db.String(128),nullable = False)
    mail_ = db.Column(db.String(48),nullable = False)
    whatsno_ = db.Column(db.String(100),nullable = False)
    auth_date = db.Column(db.DateTime(timezone=True), server_default = func.now())

    def encode_pwd(self,password):
        self.pwd_ = generate_password_hash(password)
        
    def decode_pwd(self,password):
        self.pwd_ = check_password_hash(self.pwd_password)
        
    def __repr__(self):
        return f'<user {self.user_}>'