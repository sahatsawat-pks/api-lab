import pytest

@pytest.mark.parametrize("stars, expected_result", [
    (0, 400), 
    (1, 200), 
    (5, 200), 
    (6, 400)])
def test_update_rating_range(api, auth, rating, stars, expected_result):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_result
    if expected_result == 200:
        assert res.json()["stars"] == stars
    else:
        assert "error" in res.json()