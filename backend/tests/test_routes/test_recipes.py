import json

def test_delete_recipe(client):
    data = json.dumps(
        {
            "title": "recipe_title"
        }
    )
    response = client.post("/recipes/create_recipe", data=data)
    data = json.dumps(
        {
            "id": 1
        }
    )
    response = client.delete("/recipes/delete_recipe", data=data)
    assert response.json()["title"] == "recipe_title"
    assert response.json()["id"] == 1
    assert response.status_code == 200