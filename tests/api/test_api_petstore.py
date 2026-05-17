import requests
import pytest
import logging

# Configure professional logging formatting
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

BASE_URL = "https://petstore.swagger.io/v2/pet"
TEST_PET_ID = 9876543210  
PET_NAME = "Insider QA Pet"

class TestPetstoreAPI:
    
    def test_1_create_pet_positive(self):
        logger.info(f"Starting test: CREATE positive scenario for ID {TEST_PET_ID}")
        payload = {"id": TEST_PET_ID, "name": PET_NAME, "status": "available"}
        response = requests.post(BASE_URL, json=payload)
        
        assert response.status_code == 200
        logger.info(f"CREATE successful. Status: {response.status_code}, Name: {response.json().get('name')}")

    def test_2_create_pet_negative(self):
        logger.info("Starting test: CREATE negative scenario (Invalid JSON data)")
        response = requests.post(BASE_URL, data="This is not a JSON object", headers={"Content-Type": "application/json"})
        assert response.status_code in [400, 500] 
        logger.info(f"CREATE negative caught successfully. Status: {response.status_code}")

    def test_3_read_pet_positive(self):
        logger.info(f"Starting test: READ positive scenario for ID {TEST_PET_ID}")
        response = requests.get(f"{BASE_URL}/{TEST_PET_ID}")
        assert response.status_code == 200
        logger.info(f"READ successful. Fetched ID: {response.json().get('id')}")

    def test_4_read_pet_negative(self):
        logger.info("Starting test: READ negative scenario (Non-existent ID)")
        response = requests.get(f"{BASE_URL}/000000000000") 
        assert response.status_code == 404
        logger.info(f"READ negative caught successfully. Response: {response.json().get('message')}")

    def test_5_update_pet_positive(self):
        logger.info(f"Starting test: UPDATE positive scenario for ID {TEST_PET_ID}")
        payload = {"id": TEST_PET_ID, "name": PET_NAME, "status": "sold"}
        response = requests.put(BASE_URL, json=payload)
        
        assert response.status_code == 200
        logger.info(f"UPDATE successful. New Status: {response.json().get('status')}")

    def test_6_delete_pet_positive(self):
        logger.info(f"Starting test: DELETE positive scenario for ID {TEST_PET_ID}")
        response = requests.delete(f"{BASE_URL}/{TEST_PET_ID}")
        assert response.status_code == 200
        logger.info(f"DELETE successful. Status: {response.status_code}")

    def test_7_delete_pet_negative(self):
        logger.info(f"Starting test: DELETE negative scenario (Attempting to delete already deleted ID)")
        response = requests.delete(f"{BASE_URL}/{TEST_PET_ID}")
        assert response.status_code == 404
        logger.info(f"DELETE negative caught successfully. Status: {response.status_code}")