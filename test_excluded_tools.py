import pytest

ALL_EXCLUDED = {"excludedTools": ["Knife", "Scissors", "Pizza cutter"]}
# The pizza never needs a tool that the customer excluded.
@pytest.mark.parametrize("excluded", [
    [],
    ["Knife"], ["Scissors"], ["Pizza cutter"],
    ["Knife", "Scissors"], ["Knife", "Pizza cutter"], ["Pizza cutter", "Scissors"]
])

def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded

@pytest.mark.xfail(reason="Defect 1: When there's no requirement meets pizza, it's return 500 instead of 400", strict=True)
def test_no_pizza_satisfy(api, auth):
    res = api.post("/api/pizza", json=ALL_EXCLUDED, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": "Not Found"}