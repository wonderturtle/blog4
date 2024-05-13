from flask import Blueprint
from flask import (request, session)
from flaskr.models.menu import Menu
from flaskr.models.permission import Permission
from flaskr.models.role import Role
from flaskr.models.user import User
from flask_login import current_user
import base64

# Blueprint definition
blog = Blueprint("blog", __name__, 
                 template_folder = 'templates', 
                 static_folder = 'static',
                 url_prefix = '/blog')

# --------------------------------------------------
#     TEMPORARY HERE, NEED TO FIND A BETTER WAY    |
# --------------------------------------------------
# make this global function to have in all page the sidebar
@blog.context_processor 
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
                
                if session['previous_url'].startswith('https://blog2.tomware.it'):
                    #if we are using it with plesk we need to put /app/in front of the link
                    belonging_list.append({
                        'menu_id': menu.id,
                        'belonging': menu.belonging,
                        'title': menu.title,
                        'link': f"/app{menu.link}"
                    })
            
                else:
                    belonging_list.append({
                        'menu_id': menu.id,
                        'belonging': menu.belonging,
                        'title': menu.title,
                        'link': menu.link
                    })

    return dict(sidebar_menus=menus, sidebar_belonging_list=belonging_list)

#  make this global funciton to have in all page the info of the user and the role 
@blog.context_processor 
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



from flaskr.blueprints.blog import routes