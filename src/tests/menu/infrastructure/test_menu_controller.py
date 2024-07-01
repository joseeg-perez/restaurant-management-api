from fastapi.testclient import TestClient
from apps.main import app  
from ....apps.menu.infrastructure.models.postgre_menu_model import MenuModel 
client = TestClient(app)

def test_get_all_menus():
    response = client.get("/menus")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_get_menu_by_id():
    menu_id = "some_valid_id"
    response = client.get(f"/menu/{menu_id}")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_create_menu():
    menu_data = {
        "name": "Nuevo Menú",
        "description": "Descripción del menú",
        # Agrega otros campos según tu modelo MenuModel
    }
    response = client.post("/menus", json=menu_data)
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_delete_menu():
    menu_id = "some_valid_id"
    response = client.delete(f"/menu/{menu_id}")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON
