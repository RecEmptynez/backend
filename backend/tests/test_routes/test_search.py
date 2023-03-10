import json

def test_search(client):
    # insert recipes, and ingredients
    title1 = "recipe_title"
    url1 = "recipe_url.com"
    ingredients1 = [
        "ingredient",
        "ingredient_22",
        "ingredient_33"
    ]
    data = json.dumps(
        {
            "title": title1,
            "url": url1,
            "ingredients": ingredients1
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
    assert response.json()["recipe_names"][title1] == [1,3,1/3]