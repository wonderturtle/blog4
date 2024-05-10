from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField, DateField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)

class ProfileRoleForm(Form):

    name = StringField(

        'Nome',
        id='name',
        validators=[InputRequired(), Length(min=2, max=20)],
        render_kw={'class': 'form-control', "placeholder": "Nome"}

    )

    surname = StringField(

        'Cognome', 
        id='surname',
        validators=[InputRequired(), Length(min=2, max=20)],
        render_kw={'class': 'form-control', "placeholder": "Cognome"}

    )

    username = StringField(

        'Username',
        id='username',
        validators=[InputRequired(), Length(min=2, max=20)],
        render_kw={'class': 'form-control', "placeholder": "Username"}

    )

    role_id = SelectField(
        
        'Ruolo',
        id='role_id',
        validators=[InputRequired()],
        render_kw={'class': 'form-control', "placeholder": "Ruolo"}

    )

    email = StringField(

        'Email',
        id='email',
        validators=[InputRequired(), Length(min=6, max=50)],
        render_kw={'class': 'form-control', "placeholder": "Email"}

    )
    
    submit  = SubmitField(

        'Save', id='submit',
        render_kw={'class': 'btn btn-md btn-primary', 'type':'submit'}

    )
