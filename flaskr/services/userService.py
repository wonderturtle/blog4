from flaskr.models.user import User
from flaskr import db
import flaskr.tw_globals as tw_globals
from flaskr.globals_function import process_image
from sqlalchemy.exc import SQLAlchemyError
from flask import request, session
from sqlalchemy.sql import or_
from sqlalchemy.orm import aliased
from flaskr.models.vw_user_role import UserRoleView
from datetime import datetime
from flask_login import current_user

class UserService:

    def get_all(self):
        return UserRoleView.query

    def get_user(self, id: int) -> User:
        return db.get_or_404(User, id)
    

    def get_user_by_username(self, username: str) -> User:
        return User.query.filter_by(username=username).first()
    

    # check if the username already exists, if it does, return true, else return False
    def is_username_exist(self, username: str) -> bool:
        user = self.get_user_by_username(username)
        if user:
            return True
        else:
            return False
    

    # check if the email already exists, if it does, return true, else return False
    def is_email_exist(self, email: str) -> bool:
        user = User.query.filter_by(email=email).first()
        if user:
            return True
        else:
            return False
        
    # this function is used to set all the values of the user to update
    def set_all_values_for_update(self, newUser, id: int):
        
        user = self.get_user(id)
        user.username = newUser.username
        user.m_or_f_id = newUser.m_or_f_id
        user.email = newUser.email
        user.surname = newUser.surname
        user.name = newUser.name
        user.fk_user_update = current_user.id
        user.last_update = datetime.now()
     

        if newUser.role_id:
            user.role_id = newUser.role_id

    def create_or_update(self, user: dict,id: int = None) -> None:
        """
            For creating new user or update existing user if id field is specified.
        """
        newUser = User(**user) 

        # if the id is not specified, create a new user and commit it to the database
        if not id:
            newUser.fk_user_insert = current_user.id
            newUser.fk_user_update = current_user.id
            newUser.insert_date = datetime.now()
            newUser.last_update = datetime.now()
            # check if the username already exists
            if self.is_username_exist(newUser.username):
                return ( tw_globals.RET_ALREADY_EXISTING, "Username already exists" )
            
            # check if the email already exists
            elif self.is_email_exist(newUser.email):
                return ( tw_globals.RET_ALREADY_EXISTING, "Email already exists" )
            
            # if the username and email are not existing, create a new user and commit it to the database
            else:
                try:
                    db.session.add(newUser)
                    db.session.commit()
                    return ( tw_globals.RET_CREATED, "User Created" )
                
                except Exception as e:
                    db.session.rollback()
                    return ( tw_globals.RET_DB_ERROR, e )
        
        # if the id is specified, update the existing user and commit it to the database
        else:
            try:
                self.set_all_values_for_update(newUser, id)
                db.session.commit()
                return ( tw_globals.RET_UPDATED, "User Updated" )
            
            except Exception as e:
                db.session.rollback()
                return ( tw_globals.RET_DB_ERROR, e )




    def delete(self, id: int) -> bool:
        try:
            User.query.delete(self.get_user(id))
        except Exception as e:
            print(e)
            return False

        return True
    

    def get_list(self) -> list:
        return User.query.all()


    def upload_image(self, file_data, id:int):
        '''
        this function upload the image for the user with the id passed
        first resize the image to be square and then upload it
        '''

        user = self.get_user(id)
        image_sized = process_image(file_data)
        user.image = image_sized

        try:
            db.session.commit()
            return (tw_globals.RET_UPDATED, 'Image updated')

        except SQLAlchemyError as e:
            return (tw_globals.RET_DB_ERROR, 'Database error: ' + str(e))



    def update_password(self, password, id:int):
        '''
        this function update the password for the user with the id passed
        '''
        user = self.get_user(id)
        user.password = password

        try:
            db.session.commit()
            return (tw_globals.RET_UPDATED, 'Password updated')
        
        except SQLAlchemyError as e:
            return (tw_globals.RET_DB_ERROR, 'Database error: ' + str(e))
        

    def user_datatable(self, query):
        '''
        this function is used to create the datatable for the user rendered serverside,
        require the query to filter the user result
        '''
        # Extract request parameters
        draw = int(request.form.get('draw', 0))
        start = int(request.form.get('start', 0))
        length = int(request.form.get('length', 10))
        search_value = request.form.get('search[value]', '')
        
        # Define the columns available for sorting
        # Include columns with relationships in the format 'relationship-property'
        order_columns = ['DT_RowId', 'id', 'name', 'surname','username', 'email', 'role']


        # Apply search filters if a search term is provided
        if search_value:
            # Create filters for columns using ilike to perform case-insensitive partial matching
            filters = []
            for column in order_columns[1:]:
                    # If it's not a relationship field, apply the filter to the current field
                    filters.append(getattr(UserRoleView, column).ilike(f'%{search_value}%'))

            # Apply the filters using the OR operator
            query = query.filter(or_(*filters))

        # Extract sorting information
        order_column_index = int(request.form.get('order[0][column]', 0))
        order_direction = request.form.get('order[0][dir]', 'asc')
        order_column_name = order_columns[order_column_index]


        
        # If not a column with a relationship, use the default order_column
        order_column = getattr(UserRoleView, order_column_name)


        query = query.order_by(order_column.desc() if order_direction == 'desc' else order_column)

        # Count the total number of filtered records
        filtered_records = query.count()

        # Retrieve a subset of records based on pagination parameters
        items = query.offset(start).limit(length).all()
        # Retrieve a subset of records based on pagination parameters
        previous_url = request.headers.get('Referer')
        if previous_url.startswith('https://blog2.tomware.it'):
        # Prepare the data for the DataTables response
            data_list = [
                {
                    'DT_RowId':f'{item.id}',
                    'id': f'<a href="/app/profile/detail/{item.id}"><i class="fa fa-search" aria-hidden="true"></i></a>',
                    'name': item.name,
                    'surname': item.surname,
                    'username': item.username,
                    'email': item.email,
                    'role': item.role,
                }
                for item in items
            ]
        else:
            data_list = [
                {
                    'DT_RowId':f'{item.id}',
                    'id': f'<a href="/profile/detail/{item.id}"><i class="fa fa-search" aria-hidden="true"></i></a>',
                    'name': item.name,
                    'surname': item.surname,
                    'username': item.username,
                    'email': item.email,
                    'role': item.role,
                }
                for item in items
            ]
        # Create the response dictionary
        response = {
            'draw': draw,
            'recordsTotal': filtered_records,
            'recordsFiltered': filtered_records,
            'data': data_list
        }

        # Return the response as JSON with the appropriate HTTP status and content type
        return response
        
