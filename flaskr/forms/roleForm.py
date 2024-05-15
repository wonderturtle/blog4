from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField , DateField, IntegerField,DateTimeField, SelectMultipleField)

class RoleForm(Form):
    role        = StringField(label='Ruolo',      id='role',       render_kw={'class': 'form-control'})
    start_page  = StringField(label='Start Page', id='start_page', render_kw={'class': 'form-control'})
    note        = TextAreaField(label='Note',     id='note',       render_kw={'class': 'form-control'})
    fk_user_insert              = StringField(  label = 'Inserted by',        id = 'inserted_by',        render_kw={'class': 'form-control'})
    insert_date                 = DateTimeField(label = 'Inserted on',        id = 'insert_date',        render_kw={'class': 'form-control'})
    fk_user_update              = StringField(  label = 'Updated by',         id = 'updated_by',         render_kw={'class': 'form-control'})
    last_update                 = DateTimeField(label = 'Updated on',         id = 'last_update',        render_kw={'class': 'form-control'})
