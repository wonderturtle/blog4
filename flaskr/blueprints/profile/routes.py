from flask_login import login_required, current_user
from flaskr.blueprints.profile import profile
from flask import render_template, session
from flaskr.forms.registrationForm import RegistrationForm
from flaskr.services.userService import UserService
from flaskr.services.roleService import RoleService
from flaskr.services.m_or_fService import MoFService
import flaskr.tw_globals as tw_globals
from flask import request, redirect, url_for
from flaskr.forms.profileForm import ProfileForm
from flaskr.globals_function import check_permission_r, check_permission_w
from flaskr.forms.change_passwordForm import ChangePasswordForm
import flaskr.globals_function as gf
from flaskr.forms.profile_roleForm import ProfileRoleForm
import base64

userService = UserService()
roleService = RoleService()
mofService = MoFService()

@profile.route('/profile_detail')
@login_required
@check_permission_r
def profile_detail():
    return redirect(url_for('profile.detail', id = current_user.id))

@profile.route('/detail/<int:id>')
@login_required
@check_permission_r
def detail(id):
    '''
    this route ius to access to the personal user profile
    or if the role is admin then it will access to the user profile selected
    if the role is different to admin, the user will be redirected to his profile if try to access to another profile
    '''
    if session['is_admin'] == False:
        if id != current_user.id:
            return redirect(url_for('profile.detail', id = current_user.id))
    
    msg = session.pop('msg', None)
    error = session.pop('error', None)
    user = userService.get_user(id)
    form = ChangePasswordForm(request.form)

    if user.image:
     
        image = base64.b64encode(bytes(str(user.image), 'utf-8')).decode('utf-8')
        return render_template("profile/detail.html", image = image, logged_in = True,form = form,  msg = msg, error = error, user = user, id = user.id)    
    
    return render_template("profile/detail.html",logged_in = True, form = form,  msg = msg, error = error, user = user)    



@profile.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@check_permission_r
def profile_edit(id):
    '''
    this route is to edit the user profile
    only admin can edit other users
    a non admin user can only edit his profile
    '''
    if session['is_admin'] == False:
        if id != current_user.id:
            return redirect(url_for('user.unauthorized'))
        
    msg = session.pop('msg', None)
    error = session.pop('error', None)
    user = userService.get_user(id)
    form = ProfileForm(request.form, obj=user)

    # if the user is not admin render the form without the choice of the role
    if session['is_admin'] == False:
        form = ProfileForm(request.form, obj=user)
    else:
        form = ProfileRoleForm(request.form, obj=user)
        form.role_id.choices = [(role.id, role.role) for role in roleService.get_list()]


    if request.method == 'POST':
        data = form.data
        data.pop('submit')
        code, result = userService.create_or_update(data, id)
        if code == tw_globals.RET_UPDATED:
            session['msg'] = result
            session['error'] = False
            return redirect(url_for('profile.detail', id = id))
        else:
            session['error'] = True
            session['msg'] = result
            return redirect(url_for('profile.detail', id = id))

    return render_template("user/edit.html", form = form, title = "Edit Profile", logged_in = True, msg = msg, error = error, action = 'edit')



@profile.route('/update_image/<int:id>', methods=['POST'])
@login_required
@check_permission_w
def update_user_image(id):
    '''
    This route is to update the user image, 
    first size the image to be square and then upload it
    only admin can upload other users image
    a non admin user can only upload his image
    '''
    if session['is_admin'] == False:
        if id != current_user.id:
            return redirect(url_for('user.unauthorized'))
        
    uploaded_file = request.files['file']

    if uploaded_file.filename:
        user = userService.get_user(id)

        if user:
            code, result = userService.upload_image(uploaded_file.read(), id)
            session['msg'] = result

            if code == tw_globals.RET_UPDATED:
                session['error'] = False
            
            else:
                session['error'] = True
            
            return redirect(url_for('profile.detail', id=id))
                

        else:
            return "User not found"
    else:
        return "Please provide a username and select an image file"




@profile.route('/change_password/<int:id>', methods=['GET', 'POST'])
@login_required
@check_permission_w
def change_password(id):
    '''
    this route check if the password sended is equal to the password stored in the db
    than check if the two new password match
    if all check is passed, upgrade the password
    else return error
    only admin can change other users password
    a non admin user can only change his password
    '''
    if session['is_admin'] == False:
        if id != current_user.id:
            return redirect(url_for('user.unauthorized'))

    user = userService.get_user(id)
    print(user)
    form = ChangePasswordForm(request.form)

    if request.method == 'POST' and form.validate():
        # check if the old password is equal to the password in the db 
        if user.check_password(form.old_password.data):
            # check if the two new passwords match
            if form.new_password.data == form.repeat_password.data:
                code, result = userService.update_password(form.new_password.data, id)
                session['msg'] = result

                if code == tw_globals.RET_UPDATED:
                    session['error'] = False
                
                else:
                    session['error'] = True
            
            else:
                session['msg'] = "Le paswords non corrispondono"
                session['error'] = True
            
        else:
            session['msg'] = "Vecchia password errata"
            session['error'] = True

    return redirect(url_for('profile.detail', id=id))


