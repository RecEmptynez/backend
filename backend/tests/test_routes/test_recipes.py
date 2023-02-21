import json

# test create recipe
def test_create_recipe(client):
    data = json.dumps({"title":"testrecipe","url":"testrecipe.com"})
    response = client.post("/recipes/create_recipe",content=data)
    assert response.status_code == 200 
    assert response.json()["title"] == "testrecipe"
    assert response.json()["url"] == "testrecipe.com"

# test create multiple recipes
def test_create_mult_recipes(client):
    data = json.dumps({"recipes":[{"title":"testrecipe1","url":"testrecipe1.com"},{"title":"testrecipe2","url":"testrecipe2.com"}]})
    response = client.post("/recipes/create_recipe/batch",content=data)
    assert response.status_code == 200 
    assert response.json()["recipes"][0]["title"] == "testrecipe1"
    assert response.json()["recipes"][0]["url"] == "testrecipe1.com"
    assert response.json()["recipes"][1]["title"] == "testrecipe2"
    assert response.json()["recipes"][1]["url"] == "testrecipe2.com"