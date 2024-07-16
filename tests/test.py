import os
from dotenv import load_dotenv
import requests
import pytest
import time
import json
import psycopg2


load_dotenv()

BASE_URL = os.getenv("HOST_URL")

@pytest.fixture(scope="module", autouse=True)
def wait_for_services():
    """Fixture to wait for services to be ready"""
    max_retries = 5
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(f"{BASE_URL}/")
            if response.status_code == 200 and check_db_connection():
                return
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(5)  
        retries += 1
    pytest.fail("Services did not become ready within timeout period")

def check_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DATABASE_NAME'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            host=os.getenv('DATABASE_HOST'),
            port=int(os.getenv('DATABASE_PORT'))
        )
        conn.close()
        return True
    except psycopg2.Error as err:
        print(f"Error connecting to PostgreSQL: {err}")
        return False

def test_health_check():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

def test_ask_question():
    payload = {"question": "What is AI?"}
    response = requests.post(f"{BASE_URL}/ask", json=payload)
    assert response.status_code == 200
    assert 'answer_text' in response.json()

def test_get_questions():
    response = requests.get(f"{BASE_URL}/questions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

if __name__ == "__main__":
    pytest.main()
