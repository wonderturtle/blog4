
from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField , DateField, DateTimeField, IntegerField, SelectMultipleField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL, Optional)


class UserForm(Form):
    name                       = StringField(  label = 'Name',          id = 'name',          render_kw={'class': 'form-control'})
    surname                    = StringField(  label = 'Surname',       id = 'surname',       render_kw={'class': 'form-control'})
    username                   = StringField(  label = 'Username',      id = 'username',      render_kw={'class': 'form-control'})
    password                   = PasswordField(  label = 'Password',    id = 'password',      render_kw={'class': 'form-control'})
    email                      = StringField(  label = 'Email',         id = 'email',         render_kw={'class': 'form-control'})
    note                       = TextAreaField(label = 'Note',          id = 'note',          render_kw={'class': 'form-control'})
    active                     = SelectField('Active', choices=[(1, 'True'), (0, 'False')],
                            #  option_widget=widgets.RadioInput() ,
                            #  widget=widgets.ListWidget(prefix_label=False), 
                             coerce=int, validators=[Optional()],
                             render_kw={'class': 'checkbox'})
    # fk_user_insert              = StringField(  label = 'Inserted by',        id = 'inserted_by',        render_kw={'class': 'form-control'})
    # insert_date                 = DateTimeField(label = 'Inserted on',        id = 'insert_date',        render_kw={'class': 'form-control'})
    # fk_user_update              = StringField(  label = 'Updated by',         id = 'updated_by',         render_kw={'class': 'form-control'})
    # last_update                 = DateTimeField(label = 'Updated on',         id = 'last_update',        render_kw={'class': 'form-control'})

  