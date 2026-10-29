# A second user with a name that is already taken gets status 400 and {"error": "username already taken"}.
def test_username_already_taken(api, existing_user): 
    res = api.post('/api/users', json=existing_user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}

# Logging in with a wrong password gets status 401 and {"error": "authentication failed"}.
def test_wrong_password(api, existing_user):
    res = api.post('/api/users/token/login', json={
        "username": existing_user["username"],
        "password": "WrongPassword!2026"
    })
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}

# A user with an empty name gets status 400 and {"error": "username field is empty"}.
def test_empty_username(api, existing_user):
    res = api.post('/api/users', json={
            "password": existing_user["password"]
    })
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}