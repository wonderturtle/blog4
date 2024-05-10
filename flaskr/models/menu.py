from flaskr import db
from flask_login import UserMixin

class Menu(db.Model):

    __tablename__ = 't_menu'
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title         = db.Column(db.String(255), nullable=False)
    belonging     = db.Column(db.Integer, nullable=False, default=0)
    link          = db.Column(db.String(255), nullable=False, default='null')
    order         = db.Column(db.Integer, nullable=False, default=0)
    action        = db.Column(db.String(255), nullable=False, default='null')
    icon          = db.Column(db.String(255), nullable=False, default='null')

       
    # Indexes
    __table_args__ = (
        db.Index('belonging_idx', 'belonging'),
    )