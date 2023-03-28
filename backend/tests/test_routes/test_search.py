import json

def test_search(client):
    # insert recipes, and ingredients
    title1 = "recipe_title"
    url1 = "recipe_url.com"
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
            "title": title1,
            "url": url1,
            "ingredients": ingredients1,
            "difficulty": difficulty,
            "picture_url": picture_url1,
            "rating": rating1
        }
    )
    response = client.post("/recipes/create_recipe", data=data)
    # search for the recipe
    search = json.dumps(
    {
        "max_num": count,
        "ingredient_names": [
        "ingredient"
        ]
    })

    response = client.post("/search/recipes", data=search)
    assert response.status_code == 200
    assert response.json()["recipe_names"][title1] == {'owned': 1, 'total': 2, 'url': url1, 'picture_url': picture_url1, 'difficulty': difficulty, 'rating': rating1}
