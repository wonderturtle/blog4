from flask import session, render_template, request, url_for, redirect
from flask_login import current_user
from flaskr.models.user import User
from flaskr.models.permission import Permission
from PIL import Image
from io import BytesIO
import flaskr.tw_globals as tw_globals
from sqlalchemy import and_, or_
from datetime import datetime, timedelta
from flaskr import db
from flask_wtf.csrf import generate_csrf

def check_if_user_is_admin():
    '''
    this function checks if the user is an admin by checking if the team_role_id is 1 in the session
    this parameter is stored in the session when the user logs in
    '''
    if session['role_id'] == tw_globals.ROLE_ADMIN:
        return True
    else:
        return False
    

def write_permission_in_list():
    '''
    this function is called in /auth/login route
    it takes the permission of the role of the user logged in and put them into a list

    from the permission table take all the row where the role_id is the role of the user 
    and where r is not 0
    than append in the list the menu.action related to the permission

    from the permission table take all the row where the role_id is the role of the user
    and where w is not 0
    than append in the list the menu.action related to the permission

    return two list, one for the permission r and one for the permission w

    Example permission_r: ['user', 'customer', 'feature', 'cost', 'meeting', 'grequest']
    Example permission_w: ['user', 'customer', 'grequest']
    '''

    permission_r_list = []
    permission_w_list = []

    role_id = session["role_id"]
    # take the permission of the role where r is not 0
    permissions_r = Permission.query.filter(Permission.role_id == role_id, Permission.r != 0).all()
    
    for permission in permissions_r:
        permission_r_list.append(permission.menu.action)

    # take the permission of the role where w is not 0
    permissions_w = Permission.query.filter(Permission.role_id == role_id, Permission.w != 0).all()
    for permission in permissions_w:
        permission_w_list.append(permission.menu.action)

    return permission_r_list, permission_w_list


def check_permission_r(func):
    '''
    this function check if the role of the user have the permission to read the page
    if not show an unauthorized page
    take the part of the url after the host ( in www.project.com/user/view take user ),
    if it is in the list of permission in session['permissions_r']
    then the user is allowed to see the page, else show an unauthorized page
    '''
    
    # this decorator passes along whatever arguments it receives to the original function when it calls func(*args, **kwargs).
    def wrapper(*args, **kwargs):

        permission_r_list = session['permissions_r']
        # split the url 
        path_parts = request.path.split('/')
        # check if the part of the url after the host is in the list
        if len(path_parts) > 1 and path_parts[1] in permission_r_list:
            # if it is, return the function 
            return func(*args, **kwargs)
        else:
            # if not, return an unauthorized page
            return redirect(url_for('user.unauthorized'))
        
    wrapper.__name__ = func.__name__  # This preserves the original function name
    
    # The decorator returns the wrapper function, which replaces the original function wherever the decorator is applied.
    return wrapper


def check_permission_w(func):
    '''
    this function check if the role of the user have the permission to write in the page (like insert item...)
    if not show an unauthorized page
    take the part of the url after the host  ( in www.project.com/user/view take user ),
    if it is in the list of permission in session['permissions_w']
    then the user is allowed to see the page, else show an unauthorized page
    '''

    # this decorator passes along whatever arguments it receives to the original function when it calls func(*args, **kwargs).
    def wrapper(*args, **kwargs):

        permission_w_list = session['permissions_w']
        # split the url 
        path_parts = request.path.split('/')
        # check if the part of the url after the host is in the list
        if len(path_parts) > 1 and path_parts[1] in permission_w_list:
            # if it is, return the function 
            return func(*args, **kwargs)
        else:
            # if not, return an unauthorized page
            return redirect(url_for('user.unauthorized'))
    
    wrapper.__name__ = func.__name__  # This preserves the original function name
    
    # The decorator returns the wrapper function, which replaces the original function wherever the decorator is applied.
    return wrapper



def make_square(image):
    """
    This function takes an image and converts it into a square without distortion.
    
    Arguments:
    image: PIL.Image - The input image to be squared.
    
    Returns:
    PIL.Image - The squared image.
    """
    # Get the width and height of the original image
    width, height = image.size
    
    # Determine the new size for the square image based on the maximum dimension
    new_size = max(width, height)
    
    # Create a new blank white image with the calculated new size
    new_image = Image.new("RGB", (new_size, new_size), (255, 255, 255))
    
    # Paste the original image onto the new square image, centered
    new_image.paste(image, ((new_size - width) // 2, (new_size - height) // 2))
    
    return new_image


def process_image(file_data):
    """
    This function processes an image file data to make it a square without distortion.

    Arguments:
    file_data: bytes - The raw byte data of the image file.

    Returns:
    bytes - The modified image data in bytes after making it square.
    """
    # Open the image using BytesIO to create a file-like object
    img = Image.open(BytesIO(file_data))
    
    # Make the image square using the make_square() function
    squared_img = make_square(img)

    # Convert the modified image to bytes
    img_byte_array = BytesIO()
    squared_img.save(img_byte_array, format='JPEG')  # Save the squared image as JPEG bytes
    img_byte_array = img_byte_array.getvalue()

    return img_byte_array


def advanced_search(form, model):
    '''
    This function is used for an advances search on the table passed
    the query take all the field and value and for each field-value create a filter concatenated with end in the query
    '''
    # Initialize an empty list to store the filter conditions
    filters = []

    # Loop through form fields and add conditions for non-empty and non-zero values
    for field_name, field in form._fields.items():
        if field.data not in [None, '', 0, '0', '-']:
            # Check if the field is of datetime type
            if isinstance(getattr(model, field_name).type, db.DateTime):
                # Convert the form field value to a datetime object
                start_date = datetime.combine(field.data, datetime.min.time())
                # search the current day, removing one secnd otherwise will search also the next day
                end_date = datetime.combine(field.data + timedelta(days=1), datetime.min.time()) - timedelta(seconds=1) 

                # Perform a range query for the datetime
                filters.append(getattr(model, field_name).between(start_date, end_date))
            else:
                filters.append(getattr(model, field_name) == field.data)

    # Build the final query using and_ statement
    if filters:
        query = model.query.filter(and_(*filters))
    else:
        query = model.query

    return query


def get_role_color(data):
    '''
    This function return the color of the role passed
    '''
    match data:
        case 'ADMIN':
            return 'danger'
        case 'CUSTOMER':
            return 'success'
        case 'VECTOR':
            return 'primary'

def create_badge(field, value):
    '''
    This function return an html badge with the value passed
    '''
    if field == 'role':
        color = get_role_color(value)

    return f'<span class="badge bg-{color}">{value}</span>'


def generate_serverside_datatable(query, model, fields, url_for_lens):
    '''
    this function is used to create the datatable for the user rendered serverside,
    require the query to filter the user result
    in order_columns exclude the field type we don't want to sort search ecc, like input 
    '''
    # Extract request parameters
    draw = int(request.form.get('draw', 0))
    start = int(request.form.get('start', 0))
    length = int(request.form.get('length', 10))
    search_value = request.form.get('search[value]', '')
    
    # Define the columns available for sorting
    # Include columns with relationships in the format 'relationship-property'
    # not consider upload as a data in db because is an input
    order_columns = [field['data'] for field in fields if field['data'] != 'upload']



    # Apply search filters if a search term is provided
    if search_value:
        # Create filters for columns using ilike to perform case-insensitive partial matching
        filters = []
        for column in order_columns[1:]:
                # If it's not a relationship field, apply the filter to the current field
                filters.append(getattr(model, column).ilike(f'%{search_value}%'))

        # Apply the filters using the OR operator
        query = query.filter(or_(*filters))

    # Extract sorting information
    order_column_index = int(request.form.get('order[0][column]', 0))
    order_direction = request.form.get('order[0][dir]', 'asc')
    order_column_name = order_columns[order_column_index]

    
    # If not a column with a relationship, use the default order_column
    order_column = getattr(model, order_column_name)


    query = query.order_by(order_column.desc() if order_direction == 'desc' else order_column)

    # Count the total number of filtered records
    filtered_records = query.count()

    # Retrieve a subset of records based on pagination parameters
    items = query.offset(start).limit(length).all()
    # Retrieve a subset of records based on pagination parameters

    # Prepare the data for the DataTables response
    # if the type of the field is badge, call a finction to create a span with class badge
    data_list = [
        {
            'DT_RowId':f'{item.id}',
            'id': f'<a href="{url_for_lens}{item.id}"><i class="fa fa-search" aria-hidden="true"></i></a>',

            # for item with type string will be like 'name' : item.name
            **{f'{field["data"]}': getattr(item, field["data"]) for field in fields if field["data"] not in ["DT_RowId", "id"] and field["type"] == "string"},
            
            # for item with type badge, call function to create a badge with the value of the field 
            **{f'{field["data"]}': create_badge(field["data"], getattr(item, field["data"])) for field in fields if field["type"] == "badge"},
            
            # for item with type date will be like 'date' : 2021-01-13
            **{f'{field["data"]}': f'{getattr(item, field["data"])}'[:10] for field in fields if field["type"] == "date"},

            # for item with type download show a button to download the item
            **{f'{field["data"]}': f'<a href="{field["link"]}{item.id}" class="btn btn-sm btn-primary"><i class="fa fa-download" aria-hidden="true"></i></a>' for field in fields if field["type"] == "download"},

            # for item type upload generate a inline form to upload a file
            **{f'{field["data"]}': f'''<form action="{field["link"]}" method="POST" enctype="multipart/form-data">
               <div class="custom-file w-50">
                <input type="file" name="file" class="custom-file-input">
                <label class="custom-file-label" for="customFile">Choose file</label>
               </div>
               <input type="hidden" name="id" value="{item.id}">
                <input type="hidden" name="csrf_token" value="{generate_csrf()}" />
               <button class="btn btn-sm btn-success ml-2" type="submit" value="upload"><i class="fa fa-upload" aria-hidden="true"></i></button>
               </form>'''for field in fields if field["type"] == "upload"} 
        }
        for item in items
    ]
    # print ("data list",data_list)


    # Create the response dictionary
    response = {
        'draw': draw,
        'recordsTotal': filtered_records,
        'recordsFiltered': filtered_records,
        'data': data_list
    }

    # Return the response as JSON with the appropriate HTTP status and content type
    return response
    