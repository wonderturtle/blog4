from flask import (render_template, redirect, request, url_for, session, flash,g)
from flask import jsonify
from flaskr.blueprints.user import user
from flaskr.forms.registrationForm import RegistrationForm
from flaskr.models.role import Role
from flaskr.models.user import User
from flaskr.services.userService import UserService
from flaskr.services.roleService import RoleService
from flaskr.services.m_or_fService import MoFService
import flaskr.tw_globals as tw_globals
from flask_login import login_required, current_user
from flaskr.globals_function import check_permission_r, check_permission_w, generate_serverside_datatable
from flaskr.models.vw_user_role import UserRoleView
from flaskr import db

userService = UserService()
roleService = RoleService()
mofService = MoFService()



@user.route("view", methods=["GET", "POST"])
@login_required
@check_permission_r
def view():
    '''
    this route is rendered with a view instead of a table 
    this route is to show all the users into a table
    '''
    msg = session.pop('msg', None)
    error = session.pop('error', None)
    users = UserRoleView.query.all()
    row_count = len(users)


    return render_template("user/view.html", user_list = users, tot = row_count, msg = msg, error = error)
    

@user.route('/datatable', methods=['GET', 'POST'])
@login_required
@check_permission_r
def datatable():
    fields = [
        {'data':'DT_RowId', 'type': 'string'},
        {'data':'id', 'type': 'string'},
        {'data':'name', 'type': 'string'},
        {'data':'surname', 'type': 'string'},
        {'data':'username', 'type': 'string'},
        {'data':'email', 'type': 'string'}, 
        {'data':'role', 'type': 'badge'},
    ]

    response = generate_serverside_datatable(userService.get_all(), UserRoleView, fields, "/profile/detail/")
    # response = userService.user_datatable(userService.get_all())
    return jsonify(response), 200, {'Content-Type': 'application/json'}


@user.route("/insert", methods=["GET", "POST"])
@login_required
@check_permission_w
def insert():
    '''
    this route is to insert a new user
    '''
    msg = session.pop('msg', None)
    error = session.pop('error', None)
    user_form = RegistrationForm(request.form)

    user_form.role_id.choices = [(role.id, role.role) for role in roleService.get_list()]
    user_form.m_or_f_id.choices = [(m_or_f.id, m_or_f.gender) for m_or_f in mofService.get_list()]

    if request.method == 'POST' and user_form.validate():
        data = user_form.data
        data.pop('submit')

        # create a new user
        code, result = userService.create_or_update(data)
        session['msg'] = result

        if code == tw_globals.RET_CREATED:
            session['error'] = False
        
        else:
            session['error'] = True

        return redirect(url_for('user.view'))

    return render_template("user/edit.html", msg = msg, error = error, form = user_form, title = "New User" )


@user.route("/role", methods=['POST'])
@login_required
@check_permission_r
def role():
    '''
    This route is used to get the role of a user
    fom the post request take the id of the user and get the role
    return the datail of the role in a json object
    '''
    if request.method == 'POST':
        print(request.form.get('id'))
        user = userService.get_user(request.form.get('id'))
        role = user.role
        data = [
            {'role_id': role.id, 'role': role.role, 'note': role.note},
        ]

        result = {'data': data}
        print(result)
        return jsonify(result)


@user.route('/unauthorized')
def unauthorized():
    return render_template('/user/unauthorized.html')