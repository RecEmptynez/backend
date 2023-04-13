import json

def test_search_ingredient(client):
    # insert recipes, and ingredients
    searchStr = ""
    data = json.dumps({
        "ingredient_string": searchStr
    })
    response = client.post("/search/ingredient", data = data)
    assert response.status_code == 200

    searchStr = "hfhfhfhfdhjdhfjdhfjh"
    data = json.dumps({
        "ingredient_string": searchStr
    })
    response = client.post("/search/ingredient", data=data)
    assert response.status_code == 200
    assert response.json() == []