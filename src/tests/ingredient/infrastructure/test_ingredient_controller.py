from fastapi.testclient import TestClient
from ....apps.main import app  
from ....apps.ingredient.infrastructure.models.postgre_ingredient_model import Ingredient 

client = TestClient(app)

def test_get_all_ingredients():
    response = client.get("/ingredients")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_get_ingredient_by_id():
    ingredient_id = "some_valid_id"
    response = client.get(f"/ingredient/{ingredient_id}")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_create_ingredient():
    ingredient_data = {
        "name": "Nuevo Ingrediente",
        "description": "Descripción del ingrediente",
        # Agrega otros campos según tu modelo Ingredient
    }
    response = client.post("/ingredient", json=ingredient_data)
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_delete_ingredient():
    ingredient_id = "some_valid_id"
    response = client.delete(f"/ingredient/{ingredient_id}")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON


