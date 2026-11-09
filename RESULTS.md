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
 - Block 0: 0 tools excluded ([])
 - Block 1: 1 tool excluded (["Knife"] or ["Scissors"] or ["Pizza cutter"])
 - Block 2: 2 tools excluded (e.g., ["Knife", "Scissors"])
 - Block 3: 3 tools excluded (["Knife", "Scissors", "Pizza cutter"])

## Defect report
- Title: When there's no requirement meets pizza, it's return 500 instead of 400
- Request: 
```http
  POST /api/pizza
  Content-Type: application/json
  Authorization: Bearer <token>

  {
    "excludedTools": ["Knife", "Scissors", "Pizza cutter"]
  }
```
- Expected result: 400 Bad Request ({"error": "Not Found"})
- Actual result: 500 Internal Server Error
- Severity: Medium -> While excluding all tools is an edge case, crashing with a 500 unhandled exception leaks server vulnerability details, provides zero feedback to the client, and degrades API reliability.

## Part A
- Step A4, status codes when the other user reads, changes and deletes:
```
(.venv) (base) pks_aito@Sahatsawats-MacBook-Air api-lab % pytest -s test_rating_owner.py
============================= test session starts ==============================
platform darwin -- Python 3.14.7, pytest-9.2.0, pluggy-1.7.0
rootdir: /Users/pks_aito/api-lab
plugins: metadata-3.1.1, html-4.2.0
collected 3 items                                                              

test_rating_owner.py 404
.400
.400
.

============================== 3 passed in 9.76s ===============================

```
## Part B
1. 
  - Network issues: Stubs cannot simulate real-world HTTP failures such as DNS resolution drops, TLS/SSL handshake errors, proxy timeouts, or dropped TCP connections.
  - Schema or contract mismatch with the backend/database: Stubs return canned responses based on assumptions. Real server tests detect when backend database constraints fail, when database migrations break existing queries, or when server-side business logic drifts from the stubbed contract.
2. When we use a single public token sharing in every test, it can cause race conditions problem within concurrent tests. So in project 2, we will use the split user testing for avoid this problem.
3. 

  - Reusing a requests.Session enables TCP connection pooling and HTTP keep-alive. Instead of paying the round-trip latency overhead of opening a new TCP socket, resolving DNS, and performing a TLS handshake for every individual request, requests reuse existing open sockets, drastically reducing total test run time.
  - What happened to Step 0.12: Creating a new connection for each request significantly increases run times and exposes the test suite to ephemeral port exhaustion or rate-limiting/handshake drops.
4.  
  - ```http
  POST /api/pizza
  Content-Type: application/json
  Authorization: Bearer <token>

  {
    "excludedTools": ["Knife", "Scissors", "Pizza cutter"]
  }
  ```
  - Expected result: 400 Bad Request ({"error": "Not Found"})
  - Actual result: 500 Internal Server Error
  - Severity: Medium -> While excluding all tools is an edge case, crashing with a 500 unhandled exception leaks server vulnerability details, provides zero feedback to the client, and degrades API reliability.
  - An @pytest.mark.xfail test serves as living documentation of an acknowledged bug. It continues to run in the test suite without breaking the build, alerts the team immediately if the bug gets fixed unexpectedly (XPASS), and prevents regressions once the fix is deployed.
5. 
  - Coverage
    - C1: Value of stars: 3 blocks (< 1, 1 to 5 [base], > 5)
    - C2: Type of stars: 4 blocks (whole number [base], decimal, text, missing)
    - C3: Pizza exists: 2 blocks (exists [base], does not exist)
    - C4: Token: 3 blocks (user's own [base], none, wrong length)
  - Base Choice Coverage (BCC) = 1 + (2 + 3 + 1 + 2) = 9 tests
  - All Combinations Coverage (AC) = 3 * 4 * 2 * 3 = 72 tests
6. 
  - Observed: Typically 200 OK on read, and either unhandled execution (200 OK / 500 Internal Server Error) on update and delete if authorization controls are missing.

  - Expected:
    - GET: Either 200 OK (if ratings are publicly readable) or 403 Forbidden / 404 Not Found (if ratings are private).
    - PUT / DELETE: 403 Forbidden (the authenticated user is not the owner of the resource) or 404 Not Found (to avoid leaking resource existence).
  
  - Is the difference a defect?
    - Yes, it is a Broken Object Level Authorization (BOLA / IDOR) defect. Users should never have write or delete permissions on resources owned by other users. Returning success or unhandled server crashes indicates missing access control validation on the resource ownership.
7. 
```
(.venv) (base) pks_aito@Sahatsawats-MacBook-Air api-lab % curl -H "@madeup.txt" https://quickpizza.grafana.com/api/ratings
{"ratings":[{"id":1,"stars":5,"pizza_id":1},{"id":2,"stars":1,"pizza_id":2},{"id":3,"stars":1,"pizza_id":3},{"id":5,"stars":5,"pizza_id":10},{"id":6,"stars":5,"pizza_id":12},{"id":7,"stars":5,"pizza_id":14},{"id":8,"stars":5,"pizza_id":21},{"id":9,"stars":5,"pizza_id":23},{"id":132523,"stars":2,"pizza_id":1},{"id":132524,"stars":2,"pizza_id":1},{"id":132525,"stars":2,"pizza_id":1},{"id":132526,"stars":2,"pizza_id":1},{"id":132527,"stars":2,"pizza_id":1},{"id":132528,"stars":2,"pizza_id":1},{"id":132529,"stars":2,"pizza_id":1},{"id":132530,"stars":2,"pizza_id":1},{"id":132531,"stars":2,"pizza_id":1},{"id":132532,"stars":2,"pizza_id":1},{"id":132533,"stars":2,"pizza_id":1},{"id":132534,"stars":2,"pizza_id":1},{"id":132535,"stars":2,"pizza_id":1},{"id":132536,"stars":2,"pizza_id":1},{"id":132537,"stars":2,"pizza_id":1},{"id":132538,"stars":2,"pizza_id":1},{"id":132539,"stars":2,"pizza_id":1},{"id":132540,"stars":2,"pizza_id":1},{"id":132541,"stars":2,"pizza_id":1},{"id":132542,"stars":2,"pizza_id":1},{"id":132543,"stars":2,"pizza_id":1},{"id":132544,"stars":2,"pizza_id":1},{"id":132545,"stars":2,"pizza_id":1},{"id":132546,"stars":2,"pizza_id":1},{"id":132547,"stars":2,"pizza_id":1},{"id":132548,"stars":2,"pizza_id":1},{"id":132549,"stars":2,"pizza_id":1},{"id":132550,"stars":2,"pizza_id":1},{"id":132551,"stars":2,"pizza_id":1},{"id":132553,"stars":2,"pizza_id":1},{"id":132554,"stars":2,"pizza_id":1},{"id":132555,"stars":2,"pizza_id":1},{"id":132556,"stars":2,"pizza_id":1},{"id":132557,"stars":2,"pizza_id":1},{"id":132558,"stars":2,"pizza_id":1},{"id":132559,"stars":2,"pizza_id":1},{"id":132560,"stars":2,"pizza_id":1},{"id":132561,"stars":2,"pizza_id":1},{"id":132562,"stars":2,"pizza_id":1},{"id":132563,"stars":2,"pizza_id":1},{"id":132564,"stars":2,"pizza_id":1},{"id":132565,"stars":2,"pizza_id":1}]}
```
  - The server returns 200 OK along with the list of ratings JSON data.
  - This is authentication defect, which mean the website will accept any authentication if token length is correct.
  - An attacker can forge arbitrary 16-character strings to bypass authentication barriers entirely, allowing unauthorized reading of protected user records, mass scraping, or potential account impersonation.
8. 
  - One thing an API test checks better than a web page test:
    - Validation logic and edge cases bypassing client constraints: An API test can send intentionally malformed payloads, omitted mandatory keys, or extreme boundaries directly to the endpoint—cases that client-side form validation scripts or disabled UI buttons would normally block.
  - One thing only a web page test can check:
    - End-user rendering, client-side state, and visual presentation: Checking whether CSS styling renders correctly, layout responsiveness across viewports, visual animations, DOM event propagation, or accessibility tree compliance (e.g., screen reader affordances).