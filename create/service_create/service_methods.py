# this file contains basic methods needed for one blueprint to function 
# it is used for creating new and services and appending to the already existing ones

# service_name   = input("Enter Service name (lowercase_with_underscores): ")

def service_methods(service_name): 
    # this function returns dictionary of methods
    my_methods   = {"get_list"  : f"""
    def get_list(self):
        return {service_name.title()}.query.all()
""",
"get_list_of_active" : f"""
    def get_list_of_active(self):
        '''
        return only the row where active = 1
        '''
        return {service_name.title()}.query.filter_by(active=True)
""",
"get_itemService" : f"""
    def get_itemService(self, id: int) -> {service_name.title()}:
            return {service_name.title()}.query.get_or_404(id)
    """,

"set_all_values_for_update" : f"""
    def set_all_values_for_update(self, new{service_name.title()},  id: int):
        {service_name} = self.get_itemService(id)

        {service_name}.{service_name}          = new{service_name.title()}.{service_name}
        {service_name}.note                    = new{service_name.title()}.note
        {service_name}.fk_user_update          = new{service_name.title()}.fk_user_update
        {service_name}.last_update             = new{service_name.title()}.last_update

""", 

"create_or_update" : f"""
    def create_or_update(self, {service_name}: dict, id=None) -> None:

        new{service_name.title()} = {service_name.title()}(**{service_name})

        if not id: 
            try:
                db.session.add(new{service_name.title()})
                db.session.commit()
                return (tw_globals.RET_CREATED, "{service_name.title()} Created")
            
            except Exception as e:
                db.session.rollback()
                return (tw_globals.RET_DB_ERROR, e)
            
        else:
            try:
                self.set_all_values_for_update(new{service_name.title()}, id)
                db.session.commit()
                return (tw_globals.RET_UPDATED, "{service_name.title()} Updated")
            
            except Exception as e:
                db.session.rollback()
                return (tw_globals.RET_DB_ERROR, e)

""",
"delete" : f"""
    def delete(self, id: int) -> bool:

        try:
            {service_name.title()}.query.delete(self.get_itemService(id))
            db.session.commit()
            return (tw_globals.RET_DELETED, "{service_name.title()} Deleted")
        
        except Exception as e:
            db.session.rollback()
            return (tw_globals.RET_DB_ERROR, e)
"""
}
    return my_methods