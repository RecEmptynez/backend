import json

def test_delete_recipe(client):
    title = "recipe_title"
    url = "recipe_url.com"
    ingredients = [
        "ingredient_1",
        "ingredient_2"
    ]

    data = json.dumps(
        {
            "title": title,
            "url": url,
            "ingredients": ingredients
        }
    )
    response = client.post("/recipes/create_recipe", data=data)
    data = json.dumps(
        {
            "id": 1
        }
    )
    response = client.delete("/recipes/delete_recipe", data=data)
    assert response.json()["title"] == title
    assert response.json()["url"] == url
    assert response.json()["id"] == 1
    assert response.status_code == 200

# test create recipe
def test_create_recipe(client):
    title = "recipe_title"
    url = "recipe_url.com"
    ingredients = [
        "ingredient_1",
        "ingredient_2"
    ]

    data = json.dumps(
        {
            "title": title,
            "url": url,
            "ingredients": ingredients
        }
    )    
    
    response = client.post("/recipes/create_recipe",data=data)
    assert response.status_code == 200 
    assert response.json()["title"] == title
    assert response.json()["url"] == url
    assert response.json()["ingredients"] == ingredients

# test create multiple recipes
def test_create_mult_recipes(client):
    title1 = "recipe_title"
    url1 = "recipe_url.com"
    ingredients1 = [
        "ingredient_1",
        "ingredient_2"
    ]
    title2 = "recipe_title2"
    url2 = "recipe_url2.com"
    ingredients2 = [
        "ingredient_3",
        "ingredient_4"
    ]

    data = json.dumps(
        {"recipes":
            [
                {
                    "title": title1,
                    "url": url1,
                    "ingredients": ingredients1
                },
                {
                    "title": title2,
                    "url": url2,
                    "ingredients": ingredients2
                }
            ]
        }
    )    
    response = client.post("/recipes/create_recipe/batch",data=data)
    assert response.status_code == 200 
    assert response.json()["recipes"][0]["title"] == title1
    assert response.json()["recipes"][0]["url"] == url1
    assert response.json()["recipes"][1]["title"] == title2
    assert response.json()["recipes"][1]["url"] == url2
