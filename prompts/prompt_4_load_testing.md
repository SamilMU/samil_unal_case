# AI Collaboration Iteration 4: Locust Load Test Generation

**Goal:** Generate a headless performance test using Locust to investigate the header and search module response times of `https://www.n11.com/` for a single user.

**Context provided:** The requirement asked to test the search listing functionality. I used Copilot to generate the initial Locust class and task structure, but immediately recognized a performance testing anti-pattern regarding server-side caching.

**Prompt:**
    Goal: Create a Locust load test script (locustfile.py) for n11.com.
    
    Task: 
    - Create an HttpUser class with a wait_time between 1 and 3 seconds.
    - Create Task 1: Load the homepage ("/").
    - Create Task 2: Use the search endpoint ("/arama") to search for a product (e.g., "laptop").
    - Use catch_response=True to explicitly log successes and failures.

**Output evaluation:**
- **Accepted:** The structural generation of the Locust tasks, the HTTP client calls, and the response catching block were perfectly accurate. 
- **Rejected/Refined:** The AI hardcoded the search query to `q=laptop`. I realized that hitting the same search term repeatedly would trigger n11's caching layer (Redis/Cloudflare), resulting in artificially fast response times that do not accurately test the database load. I refactored the AI's code to include a `search_terms` array and utilized Python's `random.choice()` to dynamically select a different item for every request, successfully busting the cache and simulating realistic user behavior.