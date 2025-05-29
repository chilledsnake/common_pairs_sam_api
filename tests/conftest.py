import pytest
from fastapi.testclient import TestClient
from app.main import app  # Adjust the import path according to your project structure


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
