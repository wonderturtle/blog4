from flaskr.models.permission import Permission
from flaskr import db
import flaskr.tw_globals as tw_globals
from sqlalchemy.exc import SQLAlchemyError

class PermissionService:

    # return the list of all the row
    def get_list(self) -> list:
        return Permission.query.all()
    
    # return all the permission providiing the id
    def getPermission(self, id: int) -> Permission:
        return Permission.query.get_or_404(id)

    
    # return the permission with a specific menu_id and role_id
    def get_permission_of_role(self, menu_id: int, role_id: int):
        return Permission.query.filter_by(menu_id = menu_id, role_id = role_id).first()
    

    # this function is used to set all the values of the permission to update
    def set_all_values_for_update(self, newPermission):
        permission = self.getPermission(id)
        permission.r = newPermission.r
        permission.w = newPermission.w

    
    def update_permission(self, items, role_id: int):
        """
        This method updates the permissions for a given role.

        Parameters:
        items (list): A list of tuples where each tuple contains a field and its corresponding value.
        role_id (int): The ID of the role for which the permissions are to be updated.

        Returns:
        tuple: A message indicating the status of the operation and a boolean indicating if there was an error.
        """

        # Initialize error flag as False
        error = False

        # Iterate over each field and value in items
        for field, value in items:
            # Ignore the fields 'role_id', 'note', and 'role'
            if field == 'role_id' or field == 'note' or field == 'role' or field == 'csrf_token' or field == 'start_page':
                continue

            # Split the field into menu_id and read_or_write
            menu_id, read_or_write = field.split('-')

            # Handle the hidden fields with value '0' for unchecked checkboxes
            if value == '0':
                value = 'off'

            # Fetch the permission row of the menu_id
            permission = Permission.query.filter_by(role_id=role_id, menu_id=menu_id).first()

            # If permission exists, update it
            if permission is not None:
                # Set the value to the permission
                if read_or_write == 'r':
                    permission.r = 1 if value == 'on' else 0
                elif read_or_write == 'w':
                    permission.w = 1 if value == 'on' else 0

                # Try to commit the changes to the database
                try:
                    db.session.commit()
                    msg = 'Permissions updated'
                # If an error occurs, rollback the changes and set error flag to True
                except SQLAlchemyError as e:
                    db.session.rollback()
                    error = True
                    msg = 'Failed to update permissions'
            else:
                # If there is no permission, create a new one
                permission = Permission(role_id=role_id, menu_id=menu_id)

                if read_or_write == 'r':
                    permission.r = 1 if value == 'on' else 0
                elif read_or_write == 'w':
                    permission.w = 1 if value == 'on' else 0

                # Try to add the new permission to the database and commit the changes
                try:
                    db.session.add(permission)
                    db.session.commit()
                    msg = 'Permissions created'
                # If an error occurs, rollback the changes and set error flag to True
                except SQLAlchemyError as e:
                    db.session.rollback()
                    error = True
                    msg = 'Failed to create permissions'

        # Return the status message and error flag
        return (msg, error)

    