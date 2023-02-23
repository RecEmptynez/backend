import json

def test_delete_recipe(client):
    data = json.dumps(
        {
            "title": "recipe_title",
            "url": "recipe_url.com"
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
    assert response.json()["url"] == "recipe_url.com"
    assert response.json()["id"] == 1
    assert response.status_code == 200

# test create recipe
def test_create_recipe(client):
    data = json.dumps({"title":"testrecipe","url":"testrecipe.com"})
    response = client.post("/recipes/create_recipe",data=data)
    assert response.status_code == 200 
    assert response.json()["title"] == "testrecipe"
    assert response.json()["url"] == "testrecipe.com"

# test create multiple recipes
def test_create_mult_recipes(client):
    data = json.dumps({"recipes":[{"title":"testrecipe1","url":"testrecipe1.com"},{"title":"testrecipe2","url":"testrecipe2.com"}]})
    response = client.post("/recipes/create_recipe/batch",data=data)
    assert response.status_code == 200 
    assert response.json()["recipes"][0]["title"] == "testrecipe1"
    assert response.json()["recipes"][0]["url"] == "testrecipe1.com"
    assert response.json()["recipes"][1]["title"] == "testrecipe2"
    assert response.json()["recipes"][1]["url"] == "testrecipe2.com"
