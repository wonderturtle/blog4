from flask_login import UserMixin
from flaskr import db
from datetime import datetime


class Role(db.Model):
    __tablename__       = "t_role"

    id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role                = db.Column(db.String(255), unique=True)
    start_page          = db.Column(db.String(255), default=None, nullable=True)
    note                = db.Column(db.String(255), default=None, nullable=True)
    active              = db.Column(db.Boolean,     default=True, nullable=False)
    fk_user_insert      = db.Column(db.Integer, db.ForeignKey('t_user.id'), default=0, nullable=False)
    insert_date         = db.Column(db.DateTime, nullable=False, default='1970-01-01 01:00:00')
    fk_user_update      = db.Column(db.Integer, db.ForeignKey('t_user.id'), default=0, nullable=False)
    last_update         = db.Column(db.DateTime, nullable=False, default='1970-01-01 01:00:00')
    
    # def __init__(self, role, 
    #               fk_user_insert, fk_user_update, insert_date, 
    #               start_page = '', note = '',
    #               active = True):
    #     self.role               = role
    #     self.start_page         = start_page
    #     self.note               = note
    #     self.active             = active
    #     self.fk_user_insert     = fk_user_insert
    #     self.fk_user_update     = fk_user_update
    #     self.insert_date        = insert_date
    #     self.last_update        = datetime.now()

    def __repr__(self):
        return f"id: {self.id}, name: {self.role}"