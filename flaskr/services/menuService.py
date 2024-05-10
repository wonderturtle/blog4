from flaskr.models.menu import Menu
from flaskr import db
import flaskr.tw_globals as tw_globals

class MenuService:

    # return the list of all the row with the field belonging = 0
    def list_of_menu_items(self) -> list:
       
        return Menu.query.filter_by(belonging = 0).all()

    # return all the menus 
    def get_list(self) -> list:
        return Menu.query.all()
