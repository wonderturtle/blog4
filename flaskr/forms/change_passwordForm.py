from wtforms import  (IntegerField, StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)

class ChangePasswordForm(Form):

    old_password = PasswordField(
        
        label='Old Password',
        id='old_password',
        render_kw={'class': 'form-control'}
        
    )
    
    new_password = PasswordField(
        
        label='New Password',
        id='new_password',
        render_kw={'class': 'form-control'}
    
    )
    
    repeat_password = PasswordField(
        
        label='Repeat Password',
        id='repeat_password',
        render_kw={'class': 'form-control'}
    
    )
