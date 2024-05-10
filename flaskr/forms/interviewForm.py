from wtforms import  (StringField, PasswordField, HiddenField, SubmitField, Form,  TextAreaField, SelectField, BooleanField, DateField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)
from wtforms.csrf.session import SessionCSRF
from flask import session

class InterviewForm(Form):

    company_name = StringField(
        'Nome Azienda',
        id='company_name',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Nome Azienda"}
    )

    role = StringField(
        'Mansione',
        id='role',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Mansione"}
    )

    id = HiddenField(
        'id',
        id='id',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "id"}
    )