import json

def test_search(client):
    # insert recipes, and ingredients
    title1 = "recipe_title"
    url1 = "recipe_url.com"
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
            "difficulty": difficulty
        }
    )
    response = client.post("/recipes/create_recipe", data=data)
    # search for the recipe
    search = json.dumps(
    {
        "ingredient_names": [
        "ingredient"
        ]
    })

    response = client.post("/search/recipes", data=search)
    assert response.status_code == 200
    assert response.json()["recipe_names"][title1] == {'owned': 1, 'total': 2}
