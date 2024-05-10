from flask_login import UserMixin
from flaskr import db
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 't_user'

    id           = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id      = db.Column(db.Integer, db.ForeignKey('t_role.id'), nullable=False)
    m_or_f_id    = db.Column(db.Integer, db.ForeignKey('t_m_or_f.id'), default=0, nullable=False)
    name         = db.Column(db.String(255), default=None, nullable=False)
    surname      = db.Column(db.String(255), default=None , nullable=False)
    username     = db.Column(db.String(255), nullable=False, default='')
    _password    = db.Column("password", db.String(255), default=None, nullable=False)
    email        = db.Column(db.String(255), default=None,  nullable=False)
    image        = db.Column(db.String(255), default=None , nullable=True)
    note         = db.Column(db.Text, nullable=True)
    active       = db.Column(db.Boolean, nullable=False, default=True)

    # Define relationship to roles via user_roles
    # roles = db.relationship('Role', secondary='t_role')
    role = db.relationship("Role", foreign_keys=[role_id])
    fk_user_insert      = db.Column(db.Integer, db.ForeignKey('t_user.id'), default=0, nullable=False)
    insert_date         = db.Column(db.DateTime, nullable=False, default='1970-01-01 01:00:00')
    fk_user_update      = db.Column(db.Integer, db.ForeignKey('t_user.id'), default=0, nullable=False)
    last_update         = db.Column(db.DateTime, nullable=False, default='1970-01-01 01:00:00')
    
    def __init__(self, role_id, m_or_f_id, name, surname, username, email, 
                  fk_user_insert, fk_user_update, insert_date, 
                  image = '', note = '', 
                  active = True):
        self.role_id            = role_id
        self.m_or_f_id          = m_or_f_id
        self.name               = name
        self.surname            = surname
        self.username           = username
        self.email              = email
        self.image              = image
        self.note               = note
        self.active             = active
        self.fk_user_insert     = fk_user_insert
        self.fk_user_update     = fk_user_update
        self.insert_date        = insert_date
        self.last_update        = datetime.now()

    # getter and setter for the attribute

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value, method='pbkdf2:sha256', salt_length=8)

    def check_password(self, password):
        return check_password_hash(self._password, password)


    def toJson(self):
        return {

            'name': self.name,
            'surname': self.surname,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'image': self.image,
            'note': self.note,
            'active': self.active,

        }


    # Representation of the object (Ex: When we want to print it)
    def __repr__(self):
        return f"id: {self.id} name: {self.name}, surname: {self.surname}, email: {self.email}"
