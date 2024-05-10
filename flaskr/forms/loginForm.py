from wtforms import  (StringField, PasswordField, HiddenField, SubmitField, Form,  TextAreaField, SelectField, BooleanField, DateField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)
from wtforms.csrf.session import SessionCSRF
from flask import session

# login and registration


class LoginForm(Form):

    username = StringField(

        id='username',
        validators=[InputRequired(), Length(min=2, max=50)],
        render_kw={'class': 'form-control',"placeholder": "Username"}

    )

    password = PasswordField(

            id='password',
            validators=[InputRequired(), Length(min=8, max=20)],
            render_kw={'class': 'form-control',"placeholder": "Password"}

    )

    submit = SubmitField(

            'Login',
            id='submit',
            render_kw={'class': 'btn btn-md btn-primary w-100', 'type':'submit'}

    )
