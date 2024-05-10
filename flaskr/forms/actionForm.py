from wtforms import  (StringField, PasswordField, HiddenField, SubmitField, Form,  TextAreaField, SelectField, BooleanField, DateField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)
from wtforms.csrf.session import SessionCSRF
from flask import session

class ActionForm(Form):

    action_date = DateField(
        'Data',
        id='action_date',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Data"}
    )

    outcome_insert_action = SelectField(
        'Esito',
        choices=['Lavoro', 'Tirocinio'],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Risultato"}
    )

    action_note = TextAreaField(
        'Note Azione',
        id='action_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Descrivere l’azione svolta ed eventuali note"}
    )

    outcome_insert_action_note = TextAreaField(
        'Note Esito',
        id='outcome_insert_action_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Note"}
    )

    
    id = HiddenField(
        'id',
        id='id',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "id"}
    )
