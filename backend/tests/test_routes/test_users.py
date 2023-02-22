import json

'''
def test_create_user(client):
    data = json.dumps({"username":"testuser","email":"testuser@nofoobar.com","password":"testing"})
    response = client.post("/users/",content=data)
    assert response.status_code == 200 
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True'''

def test_always_passes():
    assert True

def test_delete_recipe_ingredient(client):
    data = json.dumps(
        {
            "title": "recipe_title"
        }
    )
    response = client.post("/recipes/create_recipe", content=data)
    data = json.dumps(
        {
            "id": 1
        }
    )
    response = client.delete("/recipes/delete_recipe", content=data)
    assert response.status_code == 200
