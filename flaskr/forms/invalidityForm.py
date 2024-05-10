from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField , DateField, DateTimeField, IntegerField, SelectMultipleField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL, Optional)

class InvalidityTypeForm(Form):
    invalidity_type             = StringField(  label = 'Invalidity Type',    id = 'invalidity_type',    render_kw={'class': 'form-control'})
    invalidity_percent          = StringField(  label = 'Invalidity Perccent',id = 'invalidity_percent', render_kw={'class': 'form-control'})
    note                        = TextAreaField(label = 'Note',               id = 'note',               render_kw={'class': 'form-control'})
    active                      = SelectField('Active', choices=[(1, 'True'), (0, 'False')],
                            #  option_widget=widgets.RadioInput() ,
                            #  widget=widgets.ListWidget(prefix_label=False), 
                             coerce=int, validators=[Optional()],
                             render_kw={'class': 'checkbox'})
    fk_user_insert              = SelectField(  label = 'Inserted by',    choices=[],    id = 'inserted_by',        render_kw={'class': 'form-control'})
    insert_date                 = DateTimeField(label = 'Inserted on',        id = 'insert_date',        render_kw={'class': 'form-control'})
    fk_user_update              = SelectField(  label = 'Updated by',         choices=[],id = 'updated_by',        render_kw={'class': 'form-control'})
    last_update                 = DateTimeField(label = 'Updated on',         id = 'update_date',        render_kw={'class': 'form-control'})