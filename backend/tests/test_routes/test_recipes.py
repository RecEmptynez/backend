import json

def test_delete_recipe(client):
    title = "recipe_title"
    url = "recipe_url.com"
    picture_url1 = "picture_url.com"
    count = 1
    rating1 = "rating"
    ingredients1 = [
        ["ingredient_1", "2"],
        ["ingredient_2", "1"]
    ]
    difficulty = "medel"
    data = json.dumps(
        {
            "title": title,
            "url": url,
            "ingredients": ingredients1,
            "difficulty": difficulty,
            "picture_url": picture_url1,
            "rating": rating1
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
    assert response.json()["difficulty"] == difficulty 
    assert response.status_code == 200

# test create recipe
def test_create_recipe(client):
    title = "recipe_title"
    url = "recipe_url.com"
    picture_url1 = "picture_url.com"
    rating1 = "rating"
    ingredients1 = [
        ["ingredient_1", "2"],
        ["ingredient_2", "1"]
    ]
    difficulty = "medel"
    data = json.dumps(
        {
            "title": title,
            "url": url,
            "ingredients": ingredients1,
            "difficulty": difficulty,
            "picture_url": picture_url1,
            "rating": rating1
        }
    )
    response = client.post("/recipes/create_recipe", data=data)
    assert response.status_code == 200 
    assert response.json()["title"] == title
    assert response.json()["url"] == url
    assert response.json()["ingredients"] == ingredients1
    assert response.json()["difficulty"] == difficulty
    assert response.json()["picture_url"] == picture_url1
    assert response.json()["rating"] == rating1

# test create multiple recipes
def test_create_mult_recipes(client):
    title1 = "recipe_title"
    url1 = "recipe_url.com"
    ingredients1 = [
        ["ingredient_1", "2"],
        ["ingredient_2", "1"]
    ]
    difficulty1 = "medel"
    picture_url1 = "picture_url.com"
    rating1 = "rating"

    title2 = "recipe_title2"
    url2 = "recipe_url2.com"
    ingredients2 = [
        ["ingredient_3", "2"],
        ["ingredient_4", "1"]
    ]
    difficulty2 = "enkel"
    picture_url2 = "picture_url2.com"
    rating2 = "rating2"

    data = json.dumps(
        {"recipes":
            [
                {
                    "title": title1,
                    "url": url1,
                    "ingredients": ingredients1,
                    "difficulty": difficulty1 ,
                    "picture_url": picture_url1,
                    "rating": rating1
                },
                {
                    "title": title2,
                    "url": url2,
                    "ingredients": ingredients2,
                    "difficulty": difficulty2,
                    "picture_url": picture_url2,
                    "rating": rating2
                }
            ]
        }
    )    
    response = client.post("/recipes/create_recipe/batch",data=data)
    assert response.status_code == 200 
    assert response.json()["recipes"][0]["title"] == title1
    assert response.json()["recipes"][0]["url"] == url1
    assert response.json()["recipes"][0]["difficulty"] == difficulty1 
    assert response.json()["recipes"][0]["picture_url"] == picture_url1
    assert response.json()["recipes"][0]["rating"] == rating1   
    assert response.json()["recipes"][1]["title"] == title2
    assert response.json()["recipes"][1]["url"] == url2
    assert response.json()["recipes"][1]["difficulty"]  == difficulty2
    assert response.json()["recipes"][1]["picture_url"] == picture_url2
    assert response.json()["recipes"][1]["rating"] == rating2   
