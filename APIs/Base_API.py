import requests, os, logging
from dotenv import load_dotenv

class BaseAPI:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("BASE_API")
        self.health_check_endpoint = os.getenv("HEALTH_CHECK_ENDPOINT")

    @staticmethod
    def verify_status_code_is(expected_status_code, actual_status_code):
        try:
            assert actual_status_code == expected_status_code
            return 0
        
        except Exception as e:
            logging.warning(f"\n---verify_status_code function is filed. Expected: {expected_status_code} Actual: {actual_status_code} More: {e}")
            return 1