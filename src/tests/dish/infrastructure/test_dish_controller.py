from fastapi.testclient import TestClient
from apps.main import app
from ....apps.dish.infrastructure.models.postgre_dish_model import DishModel  

client = TestClient(app)

def test_get_all_dishes():
    response = client.get("/dishes")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_get_dish_by_id():
    dish_id = "some_valid_id"
    response = client.get(f"/dish/{dish_id}")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_create_dish():
    dish_data = {
        "name": "Nuevo Plato",
        "description": "Descripción del plato",
        "price": 10.99,
        "disponibility": True,
        "ingredients": ["ingrediente1", "ingrediente2"]
    }
    response = client.post("/dishes", json=dish_data)
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_delete_dish():
    dish_id = "some_valid_id"
    response = client.delete(f"/dish/{dish_id}")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON
