# API lab results
## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: "A White Quattro Formaggi"
- Step 0.12, results of the three runs without a session (optional): 401, 401, 200

```
============================= FAILURES =============================
__________________ test_log_in_without_a_session ___________________

    def test_log_in_without_a_session():
        name = "lab-" + uuid.uuid4().hex[:12]
        user = {"username": name, "password": "Pizza-2026"}
        res = requests.post(SITE + "/api/users", json=user)
        assert res.status_code == 201
        res = requests.post(SITE + "/api/users/token/login", json=user)
>       assert res.status_code == 200
E       assert 401 == 200
E        +  where 401 = <Response [401]>.status_code

test_no_session.py:13: AssertionError
===================== short test summary info ======================
FAILED test_no_session.py::test_log_in_without_a_session - assert 401 == 200
======================== 1 failed in 2.09s =========================
(.venv) (base) pks_aito@Sahatsawats-MacBook-Air api-lab % pytest -v test_no_session.py
======================= test session starts ========================
platform darwin -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13
cachedir: .pytest_cache
rootdir: /Users/pks_aito/api-lab
plugins: hydra-core-1.3.6, pyfakefs-5.9.3, anyio-4.15.1, cov-7.0.0
collected 1 item                                                   

test_no_session.py::test_log_in_without_a_session FAILED     [100%]

============================= FAILURES =============================
__________________ test_log_in_without_a_session ___________________

    def test_log_in_without_a_session():
        name = "lab-" + uuid.uuid4().hex[:12]
        user = {"username": name, "password": "Pizza-2026"}
        res = requests.post(SITE + "/api/users", json=user)
        assert res.status_code == 201
        res = requests.post(SITE + "/api/users/token/login", json=user)
>       assert res.status_code == 200
E       assert 401 == 200
E        +  where 401 = <Response [401]>.status_code

test_no_session.py:13: AssertionError
===================== short test summary info ======================
FAILED test_no_session.py::test_log_in_without_a_session - assert 401 == 200
======================== 1 failed in 2.07s =========================
(.venv) (base) pks_aito@Sahatsawats-MacBook-Air api-lab % pytest -v test_no_session.py
======================= test session starts ========================
platform darwin -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13
cachedir: .pytest_cache
rootdir: /Users/pks_aito/api-lab
plugins: hydra-core-1.3.6, pyfakefs-5.9.3, anyio-4.15.1, cov-7.0.0
collected 1 item                                                   

test_no_session.py::test_log_in_without_a_session PASSED     [100%]

======================== 1 passed in 1.94s =========================
```

- Step 0.16, blocks of "how many of the three tools are excluded":
## Defect report
- Title:
- Request:
- Expected result:
- Actual result:
- Severity:
## Part A
- Step A4, status codes when the other user reads, changes and deletes:
## Part B
1.
2.
3.
4.
5.
6.
7.
8.