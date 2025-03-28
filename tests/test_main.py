import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }


def test_add_sheep():
    new_sheep = {
        "id": "99",
        "name": "Fuzzy",
        "breed": "Babydoll",
        "sex": "ram"
    }

    response = client.post("/sheep", json=new_sheep)
    assert response.status_code == 201

    data = response.json()
    assert data["id"] == 99

def test_get_all_sheep():
    response = client.get("/sheep")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_update_sheep():
    # Add the sheep first so it exists
    client.post("/sheep", json={
        "id": "99",
        "name": "Fuzzy",
        "breed": "Babydoll",
        "sex": "ram"
    })

    updated_sheep = {
        "name": "Fluffy",
        "breed": "Babydoll",
        "sex": "ewe"
    }

    response = client.put("/sheep/99", json=updated_sheep)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Fluffy"


def test_delete_sheep():
    # Add the sheep first so it exists
    client.post("/sheep", json={
        "id": "99",
        "name": "Fuzzy",
        "breed": "Babydoll",
        "sex": "ram"
    })

    response = client.delete("/sheep/99")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Sheep deleted successfully"


