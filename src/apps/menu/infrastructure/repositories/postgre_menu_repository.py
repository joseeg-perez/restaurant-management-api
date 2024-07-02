from ...domain import Menu, MenuRepository
from ..models import MenuModel
from core.infrastructure.db_session.postgre_session import Session

class PostgreMenuRepository(MenuRepository):
    
    def __init__(self, menu_model):
        self.menu_model = menu_model
        self.session = Session()

    def find_all_menus(self):
        menus = self.session.query(self.menu_model).all()
        
        return menus

    def find_menu_by_id(self, id: str):
        menu = self.session.query(self.menu_model).filter_by(entity_id=id).first()

        return menu

    def save_menu(self, menu: Menu):        
        menu = MenuModel(
            name=menu.name,
            entity_id=menu._id
        )

        try: 
            self.session.add(menu)
            self.session.commit()
        
        except Exception as e:
            raise Exception(e.__str__())

    def delete_menu(self, menu: Menu):
        try:
            self.session.delete(menu)
            self.session.commit()
        except Exception as e:
            raise Exception(e.__str__())

    def update_menu(self, menu: Menu):
        pass