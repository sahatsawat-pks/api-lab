import pytest

def test_read_rating_other_user(api, other_auth, rating):
    res = api.get(f"/api/ratings/{rating['id']}", headers=other_auth)
    assert res.status_code in range (400, 500)

def test_update_rating_other_user(api, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 4}, headers=other_auth)
    assert res.status_code in range (400, 500)

def test_delete_rating_other_user(api, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    assert res.status_code in range (400, 500)