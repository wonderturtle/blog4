from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField, DateField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL)
from wtforms.csrf.session import SessionCSRF
from flask import session

class NewResumeForm(Form):

    name = StringField(
        'Nome',
        id='name',
        validators=[InputRequired()],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Nome"}
    )

    surname = StringField(
        'Cognome',
        id='surname',
        validators=[InputRequired()],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Cognome"}
    )
    
    m_or_f_id = SelectField(
        'Sesso',
        choices=[],
        render_kw={'class': 'form-control form-control-sm'}
    )

    fiscal_code = StringField(
        'Codice Fiscale',
        id='fiscal_code',
        validators=[InputRequired()],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Codice Fiscale"}
    )

    email = StringField(
        'Email',
        id='email',
        validators=[InputRequired()],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Email"}
    )

    identity_document = StringField(
        'Documento di Identità',
        id='identity_card',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Documento di Identità"}
    )


    phone = StringField(
        'Numero di Telefono',
        id='phone',
        validators=[InputRequired()],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Numero di Telefono"}
    )


    identity_document_expire_date = DateField(
        'Scad. documento',
        id='identity_document_expyre_date',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Data di Scadenza"}
    )

    # Residence part of form 
    residence_address = StringField(
        'Indirizzo',
        id='residence_adress',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Indirizzo"}
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

    residence_province_id = SelectField(
        'Provincia',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Provincia"}
    )

    residence_cap = IntegerField(
        'CAP',
        id='residence_cap',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "CAP"}
    )
    

    # Domicile part of form
    domicile_address = StringField(
        'Indirizzo',
        id='domicile_adress',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Indirizzo"}
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

    domicile_province_id = SelectField(
        'Provincia',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Provincia"}
    )

    domicile_cap = IntegerField(
        'CAP',
        id='domicile_cap',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "CAP"}
    )


    # other adress part of form
    other_address = StringField(
        'Indirizzo',
        id='other_adress',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Indirizzo"}
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

    other_address_province_id = SelectField(
        'Provincia',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Provincia"}
    )

    other_address_cap = IntegerField(
        'CAP',
        id='other_cap',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "CAP"}
    )


    birth_date = DateField(
        'Data di Nascita',
        id='birth_date',
        validators=[InputRequired()],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Data di Nascita"}
    )

    has_car = BooleanField(
        'Automunito',
        id='has_car',
        render_kw={"placeholder": "Auto"}
    )

    birth_state_id = SelectField(
        'Stato di Nascita',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Stato di Nascita"}
    )

    driving_license_type_id = SelectField(
        'Tipo di Patente',
        choices=[],
        render_kw={'class': 'form-control form-control-sm'}
    )

    birth_province_id = SelectField(
        'Provincia di Nascita',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Provincia di Nascita"}
    )


    vehicle_type_id = SelectField(
        'Disponibile a muoversi con',
        choices=[],
        render_kw={'class': 'form-control form-control-sm'}
    )

    birth_municipality_id = SelectField(
        'Comune di Nascita',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Comune di Nascita"}
    )

    citizenship_state_id = SelectField(
        'Cittadinanza',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Cittadinanza"}
    )

    # invalidity part
    ck_invalidity = BooleanField(
        'Invalidita',
        id='ck_invalidity',
        render_kw={ "placeholder": "Invalidita'"}
    )

    invalidity_type_id = SelectField(
        'Tipo di Invalidita',
        choices=[],
        render_kw={'class': 'form-control form-control-sm'}
    )

    ck_functional_diagnosis = BooleanField(
        'Diagnosi funzionale',
        id='ck_functional_diagnosis',
        render_kw={ "placeholder": "Diagnosi Funzionale"}
    )

    ck_job_placement = BooleanField(
        'Iscritto al Collocamento mirato',
        id='ck_job_placement',
        
    )

    invalidity_note = TextAreaField(
        'Note aggiuntive',
        id='invalidity_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Note"}
    )

    ck_new_poverty = BooleanField(
        'Persona inquadrabile nei fenomeni di nuova povertà ',
        id='ck_new_poverty'
    )

    ck_nomadic = BooleanField(
        'Persona Nomade',
        id='ck_nomadic'
    )

    ck_pathological_addictions = BooleanField(
        'Persona con dipendenze patologiche',
        id='ck_pathological_addictions'
    )

    ck_external_criminal_execution = BooleanField(
        'Esecuzione criminale esterna',
        id='ck_external_criminal_execution'
    )

    ck_mental_health = BooleanField(
        'Salute mentale',
        id='ck_mental_health'
    )

    ck_program_subscription = BooleanField(
        'Iscrzione a un programma',
        id='ck_program_subscription'
    )

    program_id = SelectField(
        'Programma',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Programma"}
    )

    # AREA CV
    education_level_id = SelectField(
        'Livello di Istruzione',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Livello di Istruzione"}
    )

    ck_recognition_qualification = BooleanField(
        'Riconoscimento titoli',
        id='ck_recognition_qualification',
    )

    detail_education_level = TextAreaField(
        'Dettaglio Livello di Istruzione',
        id='detail_education_level',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Dettaglio Livello di Istruzione"}
    )

    training_id = SelectField(
        'Formazione Specifica',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Formazione Specifica"}
    )

    ck_qualifications = BooleanField(
        'Abilitazioni',
        id='ck_qualifications',
    )

    
    detail_specific_training = TextAreaField(
        'Dettaglio Formazione Specifica',
        id='detail_specific_training',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Dettaglio Formazione Specifica"}
    )

    qualification_note = TextAreaField(
        'Note Abilitazioni',
        id='qualification_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Note Abilitazioni"}
    )

    ck_licenses = BooleanField(
        'Patentini',
        id='ck_licenses',
    )

    licenses_note = TextAreaField(
        'Note Patentini',
        id='licenses_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Note Patentini"}
    )

    licenses_expire_date = DateField(
        'Scad. Patentini',
        id='licenses_expire_date',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Data di Scadenza"}
    )

    ck_italian_knowledge = BooleanField(
        'Conoscenza Lingua Italiana',
        id='ck_italian_knowledge',
    )

    italian_listening_level = SelectField(
        'Ascolto',
        choices=[('','-'), ('madrelingua','Madrelingua'), ('a1','A1 - principiante'), ('a2','A2 - elementare'), ('b1','B1 - livello intermedio'), ('b2','B2 - intermedio alto'), ('c1','C1 - avanzato'), ('c2','C2 - esperto')],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Ascolto"}
    )

    italian_reading_level = SelectField(
        'Lettura',
        choices=[('','-'), ('madrelingua','Madrelingua'), ('a1','A1 - principiante'), ('a2','A2 - elementare'), ('b1','B1 - livello intermedio'), ('b2','B2 - intermedio alto'), ('c1','C1 - avanzato'), ('c2','C2 - esperto')], 
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Lettura"}
    )

    italian_writing_level = SelectField(
        'Scrittura',
        choices=[('','-'), ('madrelingua','Madrelingua'), ('a1','A1 - principiante'), ('a2','A2 - elementare'), ('b1','B1 - livello intermedio'), ('b2','B2 - intermedio alto'), ('c1','C1 - avanzato'), ('c2','C2 - esperto')],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Scrittura"}
    )

    # form for emplyment status
    employment_status_id = SelectField(
        'Stato occupazionale',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Stato occupazionale"}
    )

    end_employment_date = DateField(
        'Termine attività',
        id='end_employment_date',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Termine attività"}
    )

    note_employment_status = TextAreaField(
        'Note',
        id='note_employment_status',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Note"}
    )

    # section for work experience
    date_from = DateField(
        'Dal',
        id='date_from',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Dal"}
    )

    date_to = DateField(
        'Al',
        id='date_to',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Al"}
    )

    work_description = TextAreaField(
        'Descrizione',
        id='work_description',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Descrizione"}
    )

    work_type = SelectField(
        'Tipo',
        id='work_type',
        choices=['Lavoro', 'Volontariato', 'Tirocinio'],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Tipo"}
    )

    ck_certificate = BooleanField(
        'Certificato',
        id='ck_certificate',
    )

    # section for skills
    professional_skills = TextAreaField(
        'Competenze professionali',
        id='professional_skills',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Competenze professionali"}
    )

    soft_skills = TextAreaField(
        'Competenze personali e relazionali',
        id='soft_skills',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Competenze personali e relazionali"}
    )

    # section for professional area of interest
    job_sector_id = SelectField(
        'Settore di Interesse',
        choices=[],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Settore di Interesse"}
    )

    interest_profession_id = SelectField(
        'Professione di Interesse',
        choices=[],
        render_kw={'class': 'form-control  select-multiple',  'multiple': 'multiple', "placeholder": "Professione di Interesse"}
    )

    geographical_mobility = SelectField(
        'Mobilità Geografica',
        choices=['','Comune', 'Provincia', 'Fuori provincia'],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Mobilità Geografica"}
    )


    job_shift_id = SelectField(
        'Orario',
        choices=[],
        render_kw={'class': 'form-control  select-multiple',  'multiple': 'multiple', "placeholder": "Fascia oraria"}
    )

    geographical_mobility_note = TextAreaField(
        'Note Mobilità Geografica',
        id='geographical_mobility_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Eventuali problematiche per la distanza"}
    )

    job_shift_note = TextAreaField(
        'Note Oraria',
        id='job_shift_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Eventuali problematiche per l'orario"}
    )

    ck_weight = BooleanField(
        'Disponibile a caricare pesi',
        id='ck_weight',
    )

    ck_assist_men = BooleanField(
        'Disponibile per assistere uomini',
        id='ck_assist_men',
    )

    weight_note = TextAreaField(
        'Note',
        id='weight_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Eventuali particolarità per i pesi"}
    )

    ck_assist_couple = BooleanField(
        'Disponibile per assistere coppie',
        id='ck_assist_couple',
    )


    job_availability_id = SelectField(
        'Disponibilità al lavoro',
        choices=[],
        render_kw={'class': 'form-control select-multiple',  'multiple': 'multiple', "placeholder": "Disponibilità"}
    )

    ck_assist_disability = BooleanField(
        'Disponibile per assistere persone con disabilità',
        id='ck_assist_disability',
    )

    job_availability_note = TextAreaField(
        'Note',
        id='job_availability_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Descrivere particolari situazioni"}
    )

    ck_room_request = BooleanField(
        'Richiesta alloggio',
        id='ck_room_request',
    )

    room_request_note = TextAreaField(
        'Note',
        id='room_request_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Descrivere particolari situazioni"}
    )

    # section area of training interest
    ck_ita_language_training = BooleanField(
        'Necessità di formazione lingua italiana',
        id='ck_ita_language_training',
    )

    ck_apprenticeship = BooleanField(
        'Disponibile per tirocinio',
        id='ck_apprenticeship',
    )

    ita_language_training_note = TextAreaField(
        'Note per la lingua italiana',
        id='ita_language_training_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Specificare le modalità e l’impegno orario"}
    )

    apprenticeship_note = TextAreaField(
        'Note per il tirocinio',
        id='apprenticeship_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Specificare in che ambito"}
    )

    ck_training_course = BooleanField(
        'Disponibile per corsi di formazione',
        id='ck_training_course',
    )

    training_course_note = TextAreaField(
        'Note per corsi di formazione',
        id='training_course_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Specificare in che ambito"}
    )

    # section for search job 
    ck_user_search_job = BooleanField(
        'Ha provato a cercare lavoro',
        id='ck_user_search_job',
    )

    ck_last_6_months = BooleanField(
        'Colloqui negli ultimi 6 mesi',
        id='ck_last_6_months',
    )

    search_way = SelectField(
        'In che modo',
        choices=['-','Passaparola','Altri uffici', 'Internet/social', 'Candidatura autonoma' ],
        render_kw={'class': 'form-control select-multiple',  'multiple': 'multiple',  "placeholder": "In che modo"}
    )


    company_name = StringField(
        'Nome Azienda',
        id='company_name',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Nome Azienda"}
    )

    role = StringField(
        'Mansione',
        id='role',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Mansione"}
    )

    # section for action for the user
    action_date = DateField(
        'Data',
        id='action_date',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Data"}
    )

    outcome_insert_action = SelectField(
        'Esito',
        choices=['Lavoro', 'Tirocinio'],
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Risultato"}
    )

    action_note = TextAreaField(
        'Note Azione',
        id='action_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Descrivere l’azione svolta ed eventuali note"}
    )

    outcome_insert_action_note = TextAreaField(
        'Note Esito',
        id='outcome_insert_action_note',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Note"}
    )



    # ck_program = BooleanField(
    #     'Programma',
    #     id='ck_program',
    # )

    program_expire_date = DateField(
        'Scad. Programma',
        id='program_expire_date',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Data di Scadenza"}
    )

    active = BooleanField(
        'Attiva',
        id='active',
        render_kw={'class': 'form-control form-control-sm', "placeholder": "Attivo"}
    )




