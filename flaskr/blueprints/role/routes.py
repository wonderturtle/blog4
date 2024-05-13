from flaskr.blueprints.role import role
from flaskr.models.role import Role
from flaskr.services.roleService import RoleService
from flask import Blueprint, request, render_template, redirect, url_for, session
from flask_login import login_required
import random
from flask_login import current_user
import flaskr.tw_globals as tw_globals
from flaskr.forms.roleForm import RoleForm
from flaskr.services.menuService import MenuService
from flaskr.services.permissionService import PermissionService
from flaskr.globals_function import check_permission_r, check_permission_w

permissionService = PermissionService()
menuService = MenuService()
roleService = RoleService()

@role.route("/view", methods=["GET", "POST"])
@login_required
@check_permission_r
def view():
    '''
    this route is to show all the roles into a table
    '''
    msg = session.pop('msg', None)
    error = session.pop('error', None)
    roles = roleService.get_list()
    row_count = len(roles)
    print(f'remote address: {request.remote_addr}')
    

    return render_template("role/view.html", role_list=roles, tot=row_count, msg=msg, error=error)

@role.route("/insert", methods=["GET", "POST"])
@login_required
@check_permission_w
def role_insert():
    '''
    this route is to insert a new role
    '''
    role_form = RoleForm(request.form)
    if request.method == "POST" and role_form.validate():
        code, result = roleService.create_or_update(role_form.data)
        session['msg'] = result

        if code == tw_globals.RET_CREATED:
            session['error'] = False
        else:
            session['error'] = True

        return redirect(url_for("role.view"))
    
    return render_template("role/role_and_permission.html", role_form=role_form, action = 'insert' )


@role.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
@check_permission_w
def role_edit(id):
    '''
    this route is to edit a role and permission of its
    '''
    role = roleService.getRole(id)
    role_form = RoleForm(request.form, obj=role)

    items = []
    for menu in menuService.list_of_menu_items():
        permissions = permissionService.get_permission_of_role(menu.id, role.id)

        # The 'read' variable is assigned the value of 'permissions.r' if 'permissions' is not None, otherwise it is assigned False
        read = permissions.r if permissions else False

        # The 'write' variable is assigned the value of 'permissions.w' if 'permissions' is not None, otherwise it is assigned False
        write = permissions.w if permissions else False

        items.append((menu.title, read, write, menu.id))
    
    return render_template("role/role_and_permission.html", role_form=role_form, action = 'edit', items = items, role = role, user = current_user)


@role.route("/<int:id>", methods=["GET", "POST"])
@login_required
@check_permission_r
def role_detail(id):
    '''
    this route is to show the details of a role
    '''
    msg = session.pop('msg', None)
    error = session.pop('error', None)


    role = roleService.getRole(id)
    role_form = RoleForm(request.form, obj=role)

    # create array where to put the items of the permissions
    items = []
    for menu in menuService.list_of_menu_items():
        permissions = permissionService.get_permission_of_role(menu.id, role.id)

        # The 'read' variable is assigned the value of 'permissions.r' if 'permissions' is not None, otherwise it is assigned False
        read = permissions.r if permissions else False

        # The 'write' variable is assigned the value of 'permissions.w' if 'permissions' is not None, otherwise it is assigned False
        write = permissions.w if permissions else False

        items.append((menu.title, read, write, menu.id))
    
    return render_template("role/role_and_permission.html", role_form=role_form, action = 'read', items = items, role = role, msg = msg, error = error, user = current_user)




@role.route("/<int:id>/update", methods=["GET", "POST"])
@login_required
@check_permission_w
def role_update(id):
    '''
    step 1: 
    Update role with the value of the role_form 

    step2:
    Update a role's permissions based on the form data.

    Returns:
        redirect: A redirect to the role detail page with a success or error message.

    the request will have all the checkbox values to 0 and the checkbox checked with value = on 
    '''
    if request.method == 'POST':
        role = roleService.getRole(id)
        fole_form = RoleForm(request.form, obj=role)
        role_id = request.form.get('role_id')
        role_form_data = fole_form.data

        # update the role
        code, msg = roleService.create_or_update(role_form_data, id)
        error = True if code == tw_globals.RET_DB_ERROR else False

        msg, error = permissionService.update_permission(request.form.items(), role_id)

        session['msg'] = msg
        session['error'] = error

    return redirect(url_for("role.role_detail", id = id))
