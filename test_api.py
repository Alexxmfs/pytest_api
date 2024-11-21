import requests

BASE_URL = "http://localhost:5000/api/items"

def test_get_items():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_item():
    data = {
        "name": "Item Teste",
        "description": "Descrição do item de teste"
    }
    response = requests.post(BASE_URL, json=data)
    assert response.status_code == 201
    assert response.json().get("name") == data["name"]

def test_get_item_by_id():
    item_id = 1  
    response = requests.get(f"{BASE_URL}/{item_id}")
    assert response.status_code == 200
    assert response.json().get("id") == item_id

def test_update_item():
    item_id = 1  
    data = {
        "name": "Item Teste Atualizado",
        "description": "Descrição atualizada do item de teste"
    }
    response = requests.put(f"{BASE_URL}/{item_id}", json=data)
    assert response.status_code == 200
    assert response.json().get("name") == data["name"]

def test_delete_item():
    item_id = 1  
    response = requests.delete(f"{BASE_URL}/{item_id}")
    assert response.status_code == 204  
