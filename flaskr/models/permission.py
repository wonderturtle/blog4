from flaskr import db
from flask_login import UserMixin
from datetime import datetime

class Permission(db.Model, UserMixin):
    __tablename__ = 't_permission'

    id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id             = db.Column(db.Integer, db.ForeignKey('t_role.id'), default=0)
    menu_id             = db.Column(db.Integer, db.ForeignKey('t_menu.id'), default=0)
    r                   = db.Column(db.Integer, nullable=False, default=0)
    w                   = db.Column(db.Integer, nullable=False, default=0)
    active              = db.Column(db.Boolean, default=True, nullable=False)
    menu                = db.relationship("Menu", foreign_keys=[menu_id])
    fk_user_insert      = db.Column(db.Integer, db.ForeignKey('t_user.id'), default=0, nullable=False)
    insert_date         = db.Column(db.DateTime, nullable=False, default='1970-01-01 01:00:00')
    fk_user_update      = db.Column(db.Integer, db.ForeignKey('t_user.id'), default=0, nullable=False)
    last_update         = db.Column(db.DateTime, nullable=False, default='1970-01-01 01:00:00')
    
    # def __init__(self, role_id, menu_id,
    #               fk_user_insert, fk_user_update, insert_date, 
    #               r = False, w = False,
    #               active = True, 
    #               note = '' ):
    #     self.role_id            = role_id
    #     self.menu_id            = menu_id
    #     self.r                  = r
    #     self.w                  = w
    #     self.active             = active
    #     self.fk_user_insert     = fk_user_insert
    #     self.fk_user_update     = fk_user_update
    #     self.insert_date        = insert_date
    #     self.last_update        = datetime.now()
    #     self.note               = note
    


    def __repr__(self):
        return f"id: {self.id} role_id: {self.role_id}, menu_id: {self.menu_id}, r: {self.r}, w: {self.w}, id_user: {self.id_user}, data_ins: {self.data_ins}, data_mod: {self.data_mod}, id_user_ins: {self.id_user_ins}"
