from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField, DateField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)
from wtforms.csrf.session import SessionCSRF
from flask import session

class RegistrationForm(Form):

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

    email = StringField(

        'Email',
        id='email',
        validators=[InputRequired(), Length(min=6, max=50)],
        render_kw={'class': 'form-control', "placeholder": "Email"}

    )

    password = PasswordField(

        'Password',
        id='password',
        validators=[
            InputRequired(), Length(min=8, max=20),
            Regexp(regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[:,;@_~\\\.\-\/\+#!%*?&])[A-Za-z\d:,;@_~\\\\.-\/\+#!%*?&]{8,}$", 
                    flags=0,
                    message='Password must have minimum eight characters, at least one uppercase letter, one lowercase letter, one digit and one special character among [:;,.-_~#\@!%*?&].')],
        render_kw={'class': 'form-control', "placeholder": "Password", "type":"password"}

    )

    image = StringField(

        'Immagine Profilo', 
        id='image',
        render_kw={'class': 'form-control', "placeholder": "Immagine Profilo"}

    )

    m_or_f_id = SelectField(

        'Sesso', 
        choices=[],
        id='gender',
        render_kw={'class': 'form-control'}

    )

    role_id = SelectField(

        label = 'Ruolo',
        choices = [],
        render_kw={'class': 'form-control',"placeholder": "Ruolo"}

    )

    note = TextAreaField(

        'Note',
        id='note',
        render_kw={'class': 'form-control', "placeholder": "Note"}

    )

    active = BooleanField(

        label='Active', 
        id='active',
        render_kw={'class': 'custom-control-label'}

    )

    submit  = SubmitField(

        'Register', id='submit',
        render_kw={'class': 'btn btn-md btn-primary', 'type':'submit'}

    )

