import random
from locust import HttpUser, task, between

class N11SearchLoadTest(HttpUser):
    wait_time = between(1, 2)
    host = "https://www.n11.com"
    
    # A list of random search terms to bypass db caching
    search_terms = ["laptop", "masa", "eldiven", "kulaklik", "televizyon", "kitap"]

    @task(1)
    def load_homepage_and_header(self):
        """Simulates a user loading the homepage."""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Homepage failed to load. Status: {response.status_code}")

    @task(4)
    def search_for_product(self):
        """Simulates a user searching for random products to test DB performance."""
        # Randomly select a term for this specific request
        term = random.choice(self.search_terms)
        
        with self.client.get(f"/arama?q={term}", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Search module failed for '{term}'. Status: {response.status_code}")