from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField , DateField, IntegerField, SelectMultipleField)

class RoleForm(Form):
    role = StringField(label='Ruolo', id='role', render_kw={'class': 'form-control'})
    note = TextAreaField(label='Note', id='note', render_kw={'class': 'form-control'})
