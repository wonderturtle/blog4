from wtforms import  (StringField, PasswordField, HiddenField, SubmitField, Form,  TextAreaField, SelectField, BooleanField, DateField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)
from wtforms.csrf.session import SessionCSRF
from flask import session

class LanguageForm(Form):

    language = StringField(
        'Lingua',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Lingua"}
    )

    reading_level = SelectField(
        'Scrittura',
        choices=[('','-'), ('madrelingua','Madrelingua'), ('a1','A1 - principiante'), ('a2','A2 - elementare'), ('b1','B1 - livello intermedio'), ('b2','B2 - intermedio alto'), ('c1','C1 - avanzato'), ('c2','C2 - esperto')],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Scrittura"}
    )

    listening_level = SelectField(
        'Ascolto',
        choices=[('','-'), ('madrelingua','Madrelingua'), ('a1','A1 - principiante'), ('a2','A2 - elementare'), ('b1','B1 - livello intermedio'), ('b2','B2 - intermedio alto'), ('c1','C1 - avanzato'), ('c2','C2 - esperto')],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Ascolto"}
    )

    writing_level = SelectField(
        'Lettura',
        choices=[('','-'), ('madrelingua','Madrelingua'), ('a1','A1 - principiante'), ('a2','A2 - elementare'), ('b1','B1 - livello intermedio'), ('b2','B2 - intermedio alto'), ('c1','C1 - avanzato'), ('c2','C2 - esperto')], 
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Lettura"}
    )

    id = HiddenField(
        'id',
        id='id',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "id"}
    )

