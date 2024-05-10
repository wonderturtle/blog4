
# Define routes for your user blueprint here

from flaskr.blueprints.userbp import user_bp

from flask import (render_template, redirect, request, url_for, session, flash,g)
from flask import jsonify
from flaskr.blueprints.userbp.forms import UserForm
# from flaskr.forms.userForm import UserForm

from flaskr.models.user import User
from flaskr.services.userService import UserService
from flaskr import login_manager
from flask_login import login_user, login_required, logout_user, current_user


import flaskr.tw_globals as tw_globals
from flask_login import login_required, current_user

from flaskr import db
from datetime import datetime


userService               = UserService()


@login_manager.user_loader
@user_bp.route("/get_user/<username>", methods=["GET"])
def load_user(username):
    user = User.query.filter_by(username=username)
    print(user.id)
    # Load and return the user from the database based on user_id
    return str(user)  # Adj

  

@user_bp.route("/view", methods=["GET", "POST"])
# @login_required
# @check_permission_r
def view():
    '''
    this route is to show all the users into a table
    '''
    msg = session.pop('msg', None)
    error = session.pop('error', None)
    view_fields = userService.get_list()
#     view_fields = [  # Simulate some blog posts
#       {'name':  'Klaudija', 'surname': 'Stefan'},
#       {'name': 'Marco', 'surname': 'Content for post 2'}
#   ]
    row_count = len(view_fields)
  
    return render_template("userbp/view.html", view_fields=view_fields, tot=row_count, 
           
                           msg=msg, error=error, title = f"Users")

@user_bp.route("/insert", methods=["GET", "POST"])
# @login_required
# @check_permission_w
def insert():
    '''
    this route is to insert a new user
    '''


    form = UserForm(request.form)
    # form.fk_user_insert.data        = session['_user_id']
    # form.insert_date.data           = datetime.now()
    # form.fk_user_update.data        = 0
    # # form.last_update.data          = datetime.now()


    if request.method == "POST" and form.validate():
        
        code, result = userService.create_or_update(form.data)
       
        session['msg'] = result
       
        if code == tw_globals.RET_CREATED:
            # error = session.pop('error', None)
            session['error'] = False
            return redirect(url_for("userbp.view"))
        else:
            session['error'] = True
            return redirect(url_for('userbp.view', msg = result, error = True))

        
    
    return render_template("userbp/edit.html", form=form, action = 'insert', title = f"New User" )


@user_bp.route('/detail/<int:id>')
# @login_required
# @check_permission_r
def detail(id):
    '''
    this route is to access to the customer detail page
    it render all the information about the customer selected
    and all the project of the customer
    '''

    msg = session.pop('msg', None)
    error = session.pop('error', None)
    user = userService.get_itemService(id)

    form = UserForm(request.form, obj=user)

    return render_template("userbp/detail.html", user=user, form= form, id=id, msg = msg, error = error, title = f"User Detail")


@user_bp.route("/edit/<int:id>", methods=["GET", "POST"])
# @login_required
# @check_permission_w
def edit(id):
    '''
    this route is to edit a user and permission of its
    '''
    user = userService.get_itemService(id)
    form    = UserForm(request.form, obj=user)
    
 
 
    if request.method == "POST" and form.validate():
        form.fk_user_update.data        = session['_user_id']
        form.last_update.data           = datetime.now()

        code, result = userService.create_or_update(form.data, user.id)
       
        session['msg'] = result
       
        if code == tw_globals.RET_CREATED:
            session['error'] = False
            return redirect(url_for('user.detail', id = user.id))

        else:
            session['error'] = True
            return redirect(url_for('user.detail', id = user.id))

       
    
    return render_template("userbp/edit.html", form=form, id=id, action = 'edit',  user = user, title = f"User")



@user_bp.route('/delete/<int:id>')
# @login_required
# @check_permission_r
def delete(id):
    '''
    this route is to access to the customer detail page
    it render all the information about the customer selected
    and all the project of the customer
    '''
    msg = session.pop('msg', None)
    error = session.pop('error', None)
    user = userService.get_itemService(id)
    
   
    db.session.delete(user)
    db.session.commit()
    msg = "User Deleted"
    session['msg'] = msg

    return redirect(url_for("userbp.view"))

