import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"

# Base choice: 3 stars as a whole number, a real pizza, the user's token.
def test_base_choice_is_saved(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 201
    assert res.json()["stars"] == 3
    assert res.json()["pizza_id"] == pizza_id

# C1: a number of stars below 1 or above 5 is refused with a message.
@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range(api, auth, pizza_id, stars):
    new = {"pizza_id": pizza_id, "stars": stars}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}

# C2: a types of stars that isn't whole number is refused with a message.
@pytest.mark.parametrize("stars, expected_type", [(3.5,"number 3.5"), ("3", "string")])
def test_stars_invalid_type(api, auth, pizza_id, stars, expected_type):
    new = {"pizza_id": pizza_id, "stars": stars}
    res = api.post("/api/ratings", json=new, headers=auth)
    expected_msg = (
        f"json: cannot unmarshal {expected_type} into Go struct field Rating.stars of type int"
    )
    assert res.status_code == 400
    assert res.json() == {"error": expected_msg}

# C2: missing stars field
def test_missing_stars_field(api, auth, pizza_id):
    new = {"pizza_id": pizza_id}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}

# C3: Pizza ID doesn't exist in the system
@pytest.mark.parametrize("pizza_id", [999999999])
def test_not_exist_pizza(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": f"pizza ID {pizza_id} not found"}

# C4: No token in auth for authorization in the system

def test_no_token(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new)
    assert res.status_code == 401
    assert res.json() == {"error": f"authentication failed"}

# C4: Token wrong length
def test_token_wrong_length(api, pizza_id):
    auth = {"Authorization": "token " + "short"}
    new = {"pizza_id": pizza_id}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 401
    assert "error" in res.json()