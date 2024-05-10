from flask_login import UserMixin
from flaskr import db

class MorF(db.Model, UserMixin):
    __tablename__ = 't_m_or_f'

    id     = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gender = db.Column(db.String(255), nullable=False)