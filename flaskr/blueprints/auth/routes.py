from flaskr.blueprints.auth import auth
from flask import redirect, request, url_for, render_template, session, g
from flaskr.services.userService import UserService
from flaskr.services.roleService import RoleService
from flaskr.forms.registrationForm import RegistrationForm
from flaskr.forms.loginForm import LoginForm
from flask_login import login_user
from flaskr.globals_function import write_permission_in_list
from flaskr import login_manager
from flaskr.models.user import User

userService = UserService()
roleService = RoleService()


@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        g.user = None
    else:
        return User.query.get(int(user_id))


@auth.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id = user_id).first()


@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth.route("/login", methods=["GET", "POST"])
def login():

    msg = session.pop('msg', None)
    error = session.pop('error', None)
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user = userService.get_user_by_username(form.username.data)
        if user:
            # check if the password match
            if user.check_password(form.password.data):
                login_user(user)
                session['logged_in'] = True
                session['role_id'] = user.role_id

                # if the user is admin store is_admin as true in the session
                if user.role_id == 1:
                    session['is_admin'] = True
                else:
                    session['is_admin'] = False

                # insert the permission of the role in the session: 
                session['permissions_r'], session['permissions_w'] = write_permission_in_list()

                print(session)
                return redirect(url_for('user.view'))
            else:
                session['error'] = True
                session['msg'] = 'Password Errata'
                return redirect(url_for('auth.login'))
        else:
            session['error'] = True
            session['msg'] = 'Utente non torvato'
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html', form=form, msg=msg, error=error)

@auth.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('auth.login'))