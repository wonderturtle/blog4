from flaskr.models.role import Role
from flaskr import db
import flaskr.tw_globals as tw_globals

class RoleService:

    # return a single role by id
    def getRole(self, id: int) -> Role:
        return Role.query.get_or_404(id)
    
    
    # this function is used to set all the values of the role to update
    def set_all_values_for_update(self, newRole, id: int):
        role = self.getRole(id)
        role.role = newRole.role
        role.note = newRole.note
        

    def create_or_update(self, role: dict, id=None) -> None:

        newRole = Role(**role)

        if not id:
            try:
                db.session.add(newRole)
                db.session.commit()
                return (tw_globals.RET_CREATED, "Role Created")
            
            except Exception as e:
                db.session.rollback()
                return (tw_globals.RET_DB_ERROR, e)
            
        else:
            try:
                self.set_all_values_for_update(newRole, id)
                db.session.commit()
                return (tw_globals.RET_UPDATED, "Role Updated")
            
            except Exception as e:
                db.session.rollback()
                return (tw_globals.RET_DB_ERROR, e)



    def delete(self, id: int) -> bool:

        try:
            Role.query.delete(self.getRole(id))
        except Exception as e:
            print(e)
            return False
        return True


    def get_list(self) -> list:
        return Role.query.all()

