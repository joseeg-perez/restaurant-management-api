from fastapi.testclient import TestClient
from apps.main import app  
from ....apps.user.infrastructure.models.postgre_user_model import UserModel  

client = TestClient(app)

def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

def test_create_user():
    user_data = {
        "username": "NuevoUsuario",
        "email": "nuevo@usuario.com",
        # Agrega otros campos según tu modelo UserModel
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 200
    # Verifica más detalles según la estructura de tu respuesta JSON

