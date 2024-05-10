from flask import Blueprint
from flask_login import current_user
from flaskr.models.menu import Menu

from flaskr.models.permission import Permission
from flaskr.models.role import Role
import base64
from flaskr.models.user import User

from flask import Blueprint



user_bp = Blueprint(
        "userbp",
        __name__,
        template_folder="/flaskr/templates",
        # static_folder="flaskr/static", 
        url_prefix="/users"
    )


@user_bp.context_processor 
def inject_sidebar_items():
    menu_list = []
    #take the menu_id if the user can see or can write
    permissions = Permission.query.filter((Permission.role_id == current_user.role_id) & ((Permission.r != 0) | (Permission.w != 0))).all()
    for permission in permissions:
        menu_id = permission.menu_id
        # append the id in a list to have all the menu for a specific role
        menu_list.append(menu_id)  
    
    menus = Menu.query.filter((Menu.id.in_(menu_list)) | (Menu.belonging.in_(menu_list))).all()
    belonging_list = []
    for menu in menus:
        if menu.belonging != 0:
            belonging_list.append({
                'menu_id': menu.id,
                'belonging': menu.belonging,
                'title': menu.title,
                'link': menu.link
            })

    return dict(sidebar_menus=menus, sidebar_belonging_list=belonging_list)

from flaskr.blueprints.userbp import routes