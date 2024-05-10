import os
import re




def fix_template_syntax(text):
  # Replace "{" with "{{" and "}" with "}}"

  pattern_replace = r'(?<!\{)(?<!\{\{)(?<!\{%)\{(?!\{)(?!\%)|(?<!%\})(?<!\})(?!\%\})\}(?!\})'
  modified_text = re.sub(pattern_replace, lambda x: '{{' if x.group() == '{' else '}}', text)
    
  return modified_text
    



def create_blueprint_init(blueprint_name,  url_prefix=""):
  """
  Creates the content for the __init__.py file of a Flask blueprint.

  Args:
  blueprint_name: The name of the blueprint (lowercase with underscores).
  template_folder: The directory containing templates (default: "templates").
  static_url_path: The URL prefix for static assets (default: "assets").
  static_folder: The directory containing static files (optional).
  url_prefix: The URL prefix for blueprint routes (default: "").

  Returns:
  A string containing the content for the __init__.py file.
  """
  menu_content ="{'menu_id': menu.id,'belonging': menu.belonging,'title': menu.title,'link': menu.link}"""
  content = f"""
from flask import Blueprint
from flaskr.models.menu import Menu
from flaskr.models.permission import Permission
from flaskr.models.role import Role
from flaskr.models.user import User
from flask_login import current_user
import base64

{blueprint_name} = Blueprint(
        "{blueprint_name}",
        __name__,
        template_folder="templates",
        static_url_path='assets', 
        static_folder="flaskr/static", 
        url_prefix="/{url_prefix}"
    )


@{blueprint_name}.context_processor 
def inject_sidebar_items():
    menu_list = []
    # take the menu_id if the user can see or can write
    permissions = Permission.query.filter((Permission.role_id == current_user.role_id) & ((Permission.r != 0) | (Permission.w != 0))).all()
    for permission in permissions:
        menu_id = permission.menu_id
        # append the id in a list to have all the menu for a specific role
        menu_list.append(menu_id)  
    
    menus = Menu.query.filter((Menu.id.in_(menu_list)) | (Menu.belonging.in_(menu_list))).all()
    belonging_list = []
    for menu in menus:
        if menu.belonging != 0:
            belonging_list.append({menu_content}
            )

    return dict(sidebar_menus=menus, sidebar_belonging_list=belonging_list)

#  make this global funciton to have in all page the info of the user and the role 
@{blueprint_name}.context_processor 
def inject_user_data():
    # Get the current user from wherever you are storing it in the session
    # For example, if you are using Flask-Login, you can access it like this:
    user_logged = current_user if current_user.is_authenticated else None
    #  if the user is logged take the role_id and take the role asosciated to it
    if user_logged is not None:
        user = User.query.filter_by(id = user_logged.id).first()
        role_id = user.role_id
        role = Role.query.filter_by(id = role_id).first()

        if user.image is not None:
            image_base64 = base64.b64encode(user.image).decode('utf-8')
            return dict(user_logged=user_logged, image_base64=image_base64, role=role)
        #print(role.id)
        return dict(user_logged=user_logged, role=role)
    
    return dict(user_logged=user_logged)



from flaskr.blueprint.tables.{blueprint_name} import routes
  """

  return content


def create_blueprint_forms(blueprint_name):
   # this function returns basic content of the forms.py
  render = "{'class': 'form-control'}"
  render_checkbox = "{'class': 'checkbox'}"
  content =f"""
from wtforms import  (StringField, PasswordField, SubmitField, Form,  TextAreaField, SelectField, BooleanField , DateField, DateTimeField, IntegerField, SelectMultipleField)
from wtforms.validators import (DataRequired, InputRequired, Length, ValidationError, EqualTo, Email, Regexp, URL, Optional)


class {blueprint_name.title()}Form(Form):
    {blueprint_name}        = StringField(  label = '{blueprint_name}',    id = '{blueprint_name}',    render_kw={render})

    note                        = TextAreaField(label = 'Note',               id = 'note',               render_kw={render})
    active                      = SelectField('Active', choices=[(1, 'True'), (0, 'False')],
                            #  option_widget=widgets.RadioInput() ,
                            #  widget=widgets.ListWidget(prefix_label=False), 
                             coerce=int, validators=[Optional()],
                             render_kw={render_checkbox})
    fk_user_insert              = StringField(  label = 'Inserted by',        id = 'inserted_by',        render_kw={render})
    insert_date                 = DateTimeField(label = 'Inserted on',        id = 'insert_date',        render_kw={render})
    fk_user_update              = StringField(  label = 'Updated by',         id = 'updated_by',         render_kw={render})
    last_update                 = DateTimeField(label = 'Updated on',         id = 'last_update',        render_kw={render})

  """
  return content

def create_routes(blueprint_name):
  """
  Creates an empty routes.py file for the blueprint.

  Args:
    blueprint_name: The name of the blueprint (lowercase with underscores).

  Returns:
    A string containing the content for an empty routes.py file.
  """

  content = f"""
# Define routes for your {blueprint_name} blueprint here

from flaskr.blueprint.tables.{blueprint_name} import {blueprint_name}

from flask import (render_template, redirect, request, url_for, session, flash,g)
from flask import jsonify
from flaskr.blueprint.tables.{blueprint_name}.forms import {blueprint_name.title()}Form
# from flaskr.forms.{blueprint_name}Form import {blueprint_name.title()}Form
from flaskr.models.role import Role
from flaskr.models.user import User
from flaskr.services.userService import UserService
from flaskr.services.{blueprint_name}Service import {blueprint_name.title()}Service


import flaskr.tw_globals as tw_globals
from flask_login import login_required, current_user
from flaskr.globals_function import check_permission_r, check_permission_w, generate_serverside_datatable
from flaskr.models.vw_user_role import UserRoleView
from flaskr import db
from datetime import datetime


userService               = UserService()
{blueprint_name}Service   = {blueprint_name.title()}Service()

  

@{blueprint_name}.route("/view", methods=["GET", "POST"])
@login_required
@check_permission_r
def view():
    '''
    this route is to show all the {blueprint_name}s into a table
    '''
    msg = session.pop('msg', None)
    error = session.pop('error', None)
    view_fields = {blueprint_name}Service.get_list()
 
    row_count = len(view_fields)
  
    return render_template("{blueprint_name}/view.html", view_fields=view_fields, tot=row_count, 
           
                           msg=msg, error=error, title = f"{blueprint_name.title()}s")

@{blueprint_name}.route("/insert", methods=["GET", "POST"])
@login_required
@check_permission_w
def insert():
    '''
    this route is to insert a new {blueprint_name}
    '''


    form = {blueprint_name.title()}Form(request.form)
    form.fk_user_insert.data        = session['_user_id']
    form.insert_date.data           = datetime.now()
    form.fk_user_update.data        = 0
    # form.last_update.data          = datetime.now()


    if request.method == "POST" and form.validate():
        
        code, result = {blueprint_name}Service.create_or_update(form.data)
       
        session['msg'] = result
       
        if code == tw_globals.RET_CREATED:
            # error = session.pop('error', None)
            session['error'] = False
            return redirect(url_for("{blueprint_name}.view"))
        else:
            session['error'] = True
            return redirect(url_for('customer.view', msg = result, error = True))

        
    
    return render_template("{blueprint_name}/edit.html", form=form, action = 'insert', title = f"New {blueprint_name.title()}" )


@{blueprint_name}.route('/detail/<int:id>')
@login_required
@check_permission_r
def detail(id):
    '''
    this route is to access to the customer detail page
    it render all the information about the customer selected
    and all the project of the customer
    '''

    msg = session.pop('msg', None)
    error = session.pop('error', None)
    {blueprint_name} = {blueprint_name}Service.get_itemService(id)

    form = {blueprint_name.title()}Form(request.form, obj={blueprint_name})

    return render_template("{blueprint_name}/detail.html", {blueprint_name}={blueprint_name}, form= form, id=id, msg = msg, error = error, title = f"{blueprint_name.title()} Detail")


@{blueprint_name}.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
@check_permission_w
def edit(id):
    '''
    this route is to edit a {blueprint_name} and permission of its
    '''
    {blueprint_name} = {blueprint_name}Service.get_itemService(id)
    form    = {blueprint_name.title()}Form(request.form, obj={blueprint_name})
    
 
 
    if request.method == "POST" and form.validate():
        form.fk_user_update.data        = session['_user_id']
        form.last_update.data           = datetime.now()

        code, result = {blueprint_name}Service.create_or_update(form.data, {blueprint_name}.id)
       
        session['msg'] = result
       
        if code == tw_globals.RET_CREATED:
            session['error'] = False
            return redirect(url_for('{blueprint_name}.detail', id = {blueprint_name}.id))

        else:
            session['error'] = True
            return redirect(url_for('{blueprint_name}.detail', id = {blueprint_name}.id))

       
    
    return render_template("{blueprint_name}/edit.html", form=form, id=id, action = 'edit',  {blueprint_name} = {blueprint_name}, title = f"{blueprint_name.title()}")



@{blueprint_name}.route('/delete/<int:id>')
@login_required
@check_permission_r
def delete(id):
    '''
    this route is to access to the customer detail page
    it render all the information about the customer selected
    and all the project of the customer
    '''
    msg = session.pop('msg', None)
    error = session.pop('error', None)
    {blueprint_name} = {blueprint_name}Service.get_itemService(id)
    
   
    db.session.delete({blueprint_name})
    db.session.commit()
    msg = "{blueprint_name.title()} Deleted"
    session['msg'] = msg

    return redirect(url_for("{blueprint_name}.view"))

"""

  return content

def create_view_template(blueprint_name):
  """
  Creates a basic HTML template file.

  Args:
    template_name: The name of the template file (without extension).

  Returns:
    A string containing the content for a basic HTML template.
  """
  extends              = '{% extends "layouts/base.html" %}'
  block_title          = '{% block title %} {{ title }} {% endblock %}'
  block_content        = '{% block content %} '
  include_error        = "{% include 'includes/show_error.html' %} "
  for_item             = "{% for item in view_fields %}"
  end_for              = " {% endfor %}"
  endblock_content     = "{% endblock content %}"
  block_javascripts    = "{% block javascripts %}"
  endblock_javascrpits = "{% endblock javascripts %}"
  include_scrpits      = "{% include 'includes/datatables/style_and_script.html' %}"


  content = f"""
    {extends}

    { block_title}

    {block_content} 

      <!-- Content Wrapper. Contains page content -->
      <div class="content-wrapper">
        <!-- Content Header (Page header) -->
        <section class="content-header">
          <div class="container-fluid">
            <div class="row mb-2">
              <div class="col-sm-6">
                <h1>{{ title }}</h1>
              </div>
              <div class="col-sm-6">
                <ol class="breadcrumb float-sm-right">
                  <li class="breadcrumb-item"><a href="{{ url_for('auth.index') }}">Home</a></li>
                  <li class="breadcrumb-item active">{{ title }}</li>
                </ol>
              </div>
              
            </div>
          </div><!-- /.container-fluid -->
        </section>

        <!-- section for the buttons -->
        <section class="container-fluid">
            <a class="btn btn-app bg-primary" href="{{ url_for('{blueprint_name}.insert') }}"> 
                <i class="fa fa-file"></i>
                New
            </a>
            {include_error} 
        </section>

        <!-- Main content -->
        <section class="content">
          <div class="container-fluid">
            <div class="row">
              <div class="col-12">
                <div class="card">
                  <div class="card-header">
                    <h3 class="card-title">Totale: {{ tot }}</h3>
                  </div>
                  <!-- /.card-header -->
                  <div class="card-body">
                    <table id="{blueprint_name}Table" class="table table-striped table-bordered dataTableClass" width="100%">
                      <thead>
                      <tr>
                        <th>ID</th>
                        <th>{{ title }}</th>
        
                        <th>Note</th>
                        <th>Inserted By</th>
                        <th>Insert Date</th>
                        <th>Updated By</th>
                        <th>Update Date</th>
                      </tr>
                      </thead>
                      <tbody>
                      {for_item}
                        <tr>
                          <td><a href="{{ url_for('{blueprint_name}.detail', id=item.id) }}">
                            <i class="fa fa-search" aria-hidden="true"></i>
                          </a></td>
                          <td data-label="{blueprint_name} Level">{{ item.{blueprint_name} }}</td>
                        
                          <td data-label="Note">{{ item.note }}</td>
                          <td data-label="Inserted By"> {{ item.userinsert.name + ' ' + item.userinsert.surname }}</td>
                          <td data-label="Insert Date"> {{ item.insert_date }} </td>
                          <td data-label="Updated By">  {{ item.userupdate.name + ' ' + item.userupdate.surname }}</td>
                          <td data-label="Update Date"> {{ item.last_update }} </td>
                        </tr>
                      { end_for }
                      </tbody>
                    </table>
                  </div>
                  <!-- /.card-body -->
                </div>
                <!-- /.card -->
              </div>
              <!-- /.col -->
            </div>
            <!-- /.row -->
          </div>
          <!-- /.container-fluid -->
        </section>
        <!-- /.content -->
      </div>

    {endblock_content}

    <!-- Specific Page JS goes HERE  -->
    {block_javascripts}  
      {{ super() }}
      {include_scrpits}
    {endblock_javascrpits}

"""
  fixed_content = fix_template_syntax(content)
  return fixed_content



def create_edit_template(blueprint_name):
  """
  Creates a basic HTML template file.

  Args:
    template_name: The name of the template file (without extension).

  Returns:
    A string containing the content for a basic HTML template.
  """
  extends = '{% extends "layouts/base.html" %}'
  # block_title = '{% block title %} {{ title }} {% endblock %}'
  block_content = '{% block content %} '
  action = '{% if action == "edit" %}'
  # include_error = "{% include 'includes/show_error.html' %} "
  # for_item = "{% for item in view_fields %}"
  _else = "{% else %}"
  endif = "{% endif %}"
  for_field = '{% for field in form %}'
  end_for = " {% endfor %}"
  if_field_id = '{% if field.id not in ["submit", "id", "active", "image", "inserted_by", "updated_by", "insert_date", "last_update"] %}'
  endblock_content = "{% endblock content %}"
  block_javascripts = "{% block javascripts %}"
  endblock_javascrpits = "{% endblock javascripts %}"
  # include_scrpits = "{% include 'includes/datatables/style_and_script.html' %}"


  content = f"""
   {extends}


{block_content}    

  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1>{{ title }}</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active"> {{ title }} </li>
            </ol>
          </div>
        </div>
      </div><!-- /.container-fluid -->
    </section>

    <form action="#" method="post" >
      <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/> 
      <section class="container-fluid">
          <button class="btn btn-app bg-success ml-0" type="submit">
              <i class="fa fa-floppy-o" aria-hidden="true"></i>
              Save
          </button>
      </section>

    <!-- Main content -->
    <section class="content">
      <div class="container-fluid">
        <div class="row">
          <!-- left column -->
          <div class="col-md-12 ">
            <!-- /.card -->
            <!-- Horizontal Form -->
            <div class="card card-primary">
              <div class="card-header">
                <h3 class="card-title">
                  {action}
                  {{title}} : {{ {blueprint_name}.{blueprint_name} }}
                  {_else}
                  {{title}}
                  {endif}
                </h3>
              </div>
              <!-- /.card-header -->
                <div class="card-body">
                    {for_field}
                        {if_field_id}
                          <div class="form-group row">
                              <label for="{{field.id}}" class="col-sm-3 col-form-label" >{{ field.label }}</label>
                              <div class="col-sm-9">
                                  {{ field }}
                              </div>
                          </div>
                          
                        {endif} 
                    {end_for}
                
              
            </div>
            <!-- /.card -->
          </div>
          <!--/.col (right) -->
        </div>
        <!-- /.row -->
      </div><!-- /.container-fluid -->
    </section>
    </form>
    <!-- /.content -->
  </div>



  {endblock_content}

  <!-- Specific Page JS goes HERE  -->
  {block_javascripts}  
    {{ super() }}
    
  {endblock_javascrpits}

"""
  fixed_content=fix_template_syntax(content)
  return fixed_content


def create_detail_template(blueprint_name):
  """
  Creates a basic HTML template file.

  Args:
    template_name: The name of the template file (without extension).

  Returns:
    A string containing the content for a basic HTML template.
  """
  extends              = '{% extends "layouts/base.html" %}'
  block_title          = '{% block title %} {{ title }} {% endblock %}'
  block_content        = '{% block content %} '
  # action             = '{% if action == "edit" %}'
  include_error        = "{% include 'includes/show_error.html' %} "
  for_item_in_form     = "{% for item in form %}"
  if_item_id           = "{% if item.id not in ['submit', 'active', 'inserted_by', 'updated_by'] %}"
  elif_active          = "{% elif item.id == 'active' %}"
  elif_inserted        = "{% elif item.id == 'inserted_by' %} "
  elif_updated         = "{% elif item.id == 'updated_by' %}"
  if_item_data         = "{% if item.data == 1 %}"
  # _else              = "{% else %}"
  endif                = "{% endif %}"
  # for_field          = '{% for field in form %}'
  end_for              = " {% endfor %}"
  # if_field_id        = '{% if field.id not in ["submit", "id", "active", "image", "inserted_by", "updated_by", "insert_date", "last_update"] %}'
  endblock_content     = "{% endblock content %}"
  block_javascripts    = "{% block javascripts %}"
  endblock_javascrpits = "{% endblock javascripts %}"
  # include_scrpits    = "{% include 'includes/datatables/style_and_script.html' %}"


  content = f"""
   {extends}


 

{block_title}

{block_content}

<!-- Content Wrapper. Contains page content -->
<div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
        <div class="container-fluid">
            <div class="row mb-2">
                <div class="col-sm-6">
                    <h1>{{title}}</h1>
                </div>
                <div class="col-sm-6">
                    <ol class="breadcrumb float-sm-right">
                        <li class="breadcrumb-item"><a href="{{ url_for('auth.index') }}">Home</a></li>
                        <li class="breadcrumb-item active">{{title }}</li>
                    </ol>
                </div>
            </div>
        </div>
    </section>



    <section class="container-fluid">
        <a class="btn btn-app bg-primary" href="{{ url_for('{blueprint_name}.edit', id={blueprint_name}.id) }}"> 
            <i class="fa fa-file"></i>
            Edit
        </a>

        
        <a class="btn btn-app bg-danger" href="{{ url_for('{blueprint_name}.delete', id={blueprint_name}.id) }}"> 
            <i class="fa fa-trash"></i>
            Delete
        </a>
        

        <a class="btn btn-app bg-primary" href="{{ url_for('{blueprint_name}.view') }}"> 
            <i class="fa fa-undo"></i>
            Back
        </a>
        {include_error}  
    </section>
    

    <section class="container-fluid">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="card">
                        <div class="card-header bg-primary">
                            <h3 class="card-title">{{ {blueprint_name}.{blueprint_name}}}</h3>
                            
                            <div class="card-tools">
                                <button type="button" class="btn btn-tool" data-card-widget="collapse" title="Collapse">
                                    <i class="fas fa-minus"></i>
                                </button>
                                <button type="button" class="btn btn-tool" data-card-widget="remove" title="Remove">
                                    <i class="fas fa-times"></i>
                                </button>
                            </div>
                        </div>
                        <div class="card-body">
                            {for_item_in_form}
                                {if_item_id}
                                    <div class="form-group row">
                                        <label class="col-sm-2 col-form-label">{{item.label}}</label>
                                        <div class="col-sm-10">
                                            <input type="text" class="form-control" name="{{ item.name }}"  id="{{ item.id }}" value="{{ item.data }}" disabled  >
                                        </div>
                                    </div>
                                {elif_active}
                                    <div class="form-group row">
                                        <label class="col-sm-2 col-form-label">{{item.label}}</label>
                                        <div class="col-sm-10">
                                            <input type="checkbox" name="{{ item.name }}"  id="{{ item.id }}" value="{{ item.data }}" disabled {if_item_data} checked {endif} >
                                        </div>
                                    </div>
                                    {elif_inserted}
                                    <div class="form-group row">
                                        <label class="col-sm-2 col-form-label">{{item.label}}</label>
                                        <div class="col-sm-10">
                                            <input type="text" class="form-control" name="{{ item.name }}"  id="{{ item.id }}"  value="{{{blueprint_name}.userinsert.name + ' ' + {blueprint_name}.userinsert.surname}}" disabled  >
                                         
                                        </div>
                                    </div>
                                    {elif_updated}
                                    <div class="form-group row">
                                        <label class="col-sm-2 col-form-label">{{item.label}}</label>
                                        <div class="col-sm-10">
                                            <input type="text" class="form-control" name="{{ item.name }}"  id="{{ item.id }}"  value="{{{blueprint_name}.userupdate.name + ' ' + {blueprint_name}.userupdate.surname}}" disabled  >
                                         
                                        </div>
                                    </div>
                                {endif}
                            {end_for}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</div>


  {endblock_content}

  <!-- Specific Page JS goes HERE  -->
  {block_javascripts}  
    {{ super() }}
    
  {endblock_javascrpits}

"""
  fixed_content = fix_template_syntax(content)
  return fixed_content




def create_blueprint_content(blueprint_name, path=".", url_prefix = ""):
  """
  Creates a new blueprint directory structure with basic files.

  Args:
    blueprint_name: The name of the blueprint (lowercase with underscores).
    path: The directory path to create the blueprint structure (default: current directory).
    template_name: The name of the initial template to create (default: "home").
  """

  # Create blueprint directory
  blueprint_dir = os.path.join(path, blueprint_name)
  os.makedirs(blueprint_dir, exist_ok=True)

  # Create __init__.py file
  init_content = create_blueprint_init(blueprint_name, url_prefix=url_prefix)
  with open(os.path.join(blueprint_dir, "__init__.py"), 'w', encoding='utf-8') as f:
    f.write(init_content)

  # Create routes.py file
  routes_content = create_routes(blueprint_name)
  with open(os.path.join(blueprint_dir, "routes.py"), 'w', encoding='utf-8') as f:
    f.write(routes_content)
  # Creates forms.py
  forms_content = create_blueprint_forms(blueprint_name)
  with open(os.path.join(blueprint_dir, "forms.py"), 'w', encoding='utf-8') as f:
    f.write(forms_content)
  # Create templates directory
  templates_dir = os.path.join(blueprint_dir, f"templates", blueprint_name)
  os.makedirs(templates_dir, exist_ok=True)

  # Create initial template file
  template_view_content = create_view_template(blueprint_name)
  with open(os.path.join(templates_dir, f"view.html"), 'w', encoding='utf-8') as f:
    f.write(template_view_content)

  template_edit_content = create_edit_template(blueprint_name)
  with open(os.path.join(templates_dir, f"edit.html"), 'w', encoding='utf-8') as f:
    f.write(template_edit_content)

  template_detail_content = create_detail_template(blueprint_name)
  with open(os.path.join(templates_dir, f"detail.html"), 'w', encoding='utf-8') as f:
    f.write(template_detail_content)
  

  print(f"Blueprint folder '{blueprint_name}' created successfully!")


if __name__ == "__main__":
  blueprint_name = input("Enter blueprint name (lowercase_with_underscores): ")
  blueprint_path = input("Enter path to create the blueprint (e.g., blueprints): ")
  url_prefix     = input("Enter prefix for the url for the blueprint (e.g., auth): ")
  create_blueprint_content(blueprint_name, blueprint_path, url_prefix)
