from fastapi.testclient import TestClient
from ....main import app 

client = TestClient(app)

def test_get_all_products():
    response = client.get("/products")
    assert response.status_code == 200

def test_get_product_by_id():
    test_id = "1"  # reemplazar con un id válido en la base de datos
    response = client.get(f"/product/{test_id}")
    assert response.status_code == 200

def test_create_product():
    test_product = {"id": "Test Product", "name": "This is a test product", "price":"1289", "stock":"37182"}  # reemplazar con los datos del producto
    response = client.post("/products", json=test_product)
    assert response.status_code == 200

def test_delete_product():
    test_id = "1"  # reemplazar con un id válido en la base de datos
    response = client.delete(f"/product/{test_id}")
    assert response.status_code == 200
