import json


def test_create_user(client):
    data = json.dumps({"username":"testuser","email":"testuser@nofoobar.com","password":"testing"})
    response = client.post("/users/",content=data)
    assert response.status_code == 200 
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True