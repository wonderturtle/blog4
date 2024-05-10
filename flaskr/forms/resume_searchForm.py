from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField, DateField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)
from wtforms.csrf.session import SessionCSRF
from flask import session

class ResumeSearchForm(Form):

    name = StringField(
        'Nome',
        id='name',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Nome"}
    )

    surname = StringField(
        'Cognome',
        id='surname',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Cognome"}
    )

    citizenship_state_id = SelectField(
        'Cittadinanza',
        id='citizenship_state_id',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Cittadinanza"}
    )

    birth_state_id = SelectField(
        'Stato di nascita',
        id='birth_state_id',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Luogo di nascita"}
    )

     # Residence part of form 
    residence_province_id = SelectField(
        'Provincia',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Provincia"}
    )
    residence_municipality_id = SelectField(
        'Comune',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Comune"}
    )

    residence_place_id = SelectField(
        'Località',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Località"}
    )


    # Domicile part of form
    
    domicile_province_id = SelectField(
        'Provincia',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Provincia"}
    )

    domicile_municipality_id = SelectField(
        'Comune',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Comune"}
    )

    domicile_place_id = SelectField(
        'Località',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Località"}
    )



    # other adress part of form
    
    other_address_province_id = SelectField(
        'Provincia',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Provincia"}
    )


    other_address_municipality_id = SelectField(
        'Comune',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Comune"}
    )

    other_address_place_id = SelectField(
        'Località',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Località"}
    )

    m_or_f_id = SelectField(
        'Sesso',
        choices=[],
        render_kw={'class': 'form-control form-control-sm'}
    )

    birth_date = DateField(
        'Data di Nascita',
        id='birth_date',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Data di Nascita"}
    )

    driving_license_type_id = SelectField(
        'Tipo di Patente',
        choices=[],
        render_kw={'class': 'form-control form-control-sm'}
    )

    has_car = BooleanField(
        'Automunito',
        id='has_car',
        render_kw={"placeholder": "Auto"}
    )

    education_level_id = SelectField(
        'Livello di Istruzione',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Livello di Istruzione"}
    )

    training_id = SelectField(
        'Formazione Specifica',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Formazione Specifica"}
    )

    ck_licenses = BooleanField(
        'Patentini',
        id='ck_licenses',
    )

    interest_profession_id = SelectField(
        'Professione di Interesse',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Professione di Interesse"}
    )

    employment_status_id = SelectField(
        'Stato occupazionale',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Stato occupazionale"}
    )

    geographical_mobility = SelectField(
        'Mobilità Geografica',
        choices=['','Comune', 'Provincia', 'Fuori provincia'],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Mobilità Geografica"}
    )


    job_shift_id = SelectField(
        'Disponibilità oraria',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Fascia oraria"}
    )

    
    ck_weight = BooleanField(
        'Disponibile a caricare pesi',
        id='ck_weight',
    )

    ck_assist_men = BooleanField(
        'Disponibile per assistere uomini',
        id='ck_assist_men',
    )

    ck_assist_couple = BooleanField(
        'Disponibile per assistere coppie',
        id='ck_assist_couple',
    )
    
    ck_assist_disability = BooleanField(
        'Disponibile per assistere persone con disabilità',
        id='ck_assist_disability',
    )

    job_availability_id = SelectField(
        'Disponibilità al lavoro',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Disponibilità"}
    )

    ck_apprenticeship = BooleanField(
        'Disponibile per tirocinio',
        id='ck_apprenticeship',
    )

    ck_training_course = BooleanField(
        'Disponibile per corsi di formazione',
        id='ck_training_course',
    )

    fiscal_code = StringField(
        'Codice Fiscale',
        id='fiscal_code',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Codice Fiscale"}
    )



