import requests, os, logging
from dotenv import load_dotenv


class BaseAPI:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("BASE_API")
        self.health_check_endpoint = os.getenv("HEALTH_CHECK_ENDPOINT")
        self.user_register_endpoint = os.getenv("USER_REGISTER_ENDPOINT")
        self.user_login_endpoint = os.getenv("USER_LOGIN_ENDPOINT")
        self.user_delete_endpoint = os.getenv("USER_DELETE_ENDPOINT")
        self.user_profile_endpoint = os.getenv("USER_PROFILE_ENDPOINT")
        self.user_edit_profile_endpoint = os.getenv("USER_PROFILE_ENDPOINT")
        self.user_logout_endpoint = os.getenv("USER_LOGOUT_ENDPOINT")
        self.notes_endpoint = os.getenv("NOTES_ENDPOINT")
        self.name = os.getenv("NAME")
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.phone = os.getenv("PHONE")
        self.company = os.getenv("COMPANY")
        self.home_note_title = os.getenv("HOME_NOTE_TITLE")
        self.home_note_description = os.getenv("HOME_NOTE_DESCRIPTION")
        self.home_note_category = os.getenv("HOME_NOTE_CATEGORY")
        self.work_note_title = os.getenv("WORK_NOTE_TITLE")
        self.work_note_description = os.getenv("WORK_NOTE_DESCRIPTION")
        self.work_note_category = os.getenv("WORK_NOTE_CATEGORY")
        self.personal_note_title = os.getenv("PERSONAL_NOTE_TITLE")
        self.personal_note_description = os.getenv("PERSONAL_NOTE_DESCRIPTION")
        self.personal_note_category = os.getenv("PERSONAL_NOTE_CATEGORY")


    @staticmethod
    def verify_status_code_is(expected_status_code, actual_status_code):
        try:
            assert actual_status_code == expected_status_code
            return 0
        
        except Exception as e:
            logging.warning(f"\n---verify_status_code function is filed. Expected:{expected_status_code} Actual:{actual_status_code} More: {e}")
            return 1


    def verify_health_check(self):
        url = f"{self.host}{self.health_check_endpoint}"
        response = requests.get(url=url)
        try:
            assert response.json()["success"] == True
            assert response.json()["status"] == 200
            assert response.json()["message"] == "Notes API is Running"
            return 0

        except Exception as e:
            logging.warning(f"---Health_checking_was_failed!!! Exception: {e}")
            return 1


    @staticmethod
    def get_default_header_with_auth(token):
        header = {
            "Content-Type": "application/json",
            "x-auth-token": token
        }
        return header
