from flask_login import UserMixin
from flaskr import db
# from flaskr.models.role import Role
# from flaskr.models.user import User

class UserRoleView(db.Model):
    __tablename__ = 'vw_user_role'

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(255))
    surname    = db.Column(db.String(255))
    username   = db.Column(db.String(255))
    email      = db.Column(db.String(255))
    role       = db.Column(db.String(255))
    gender     = db.Column(db.String(255))

    def __repr__(self):
        return f"<UserRoleView {self.username}>"
