import pytest
from fastapi.testclient import TestClient
from ..apps.main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client: #Proporciona un cliente de prueba para la base de datos
        yield test_client

@pytest.fixture(scope="module")
def test_db():
    # Configurar la base de datos de prueba aquí
    pass

@pytest.fixture(scope="module")
def auth_token():
    # Crea un token de autenticación de prueba aquí
    return "test-token"