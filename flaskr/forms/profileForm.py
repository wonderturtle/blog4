from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField, DateField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)

class ProfileForm(Form):

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
    
    submit  = SubmitField(

        'Salva', id='submit',
        render_kw={'class': 'btn btn-md btn-primary', 'type':'submit'}

    )
