import requests, logging
from APIs.Base_API import BaseAPI

class NotesAPI(BaseAPI):

    def call_create_notes_api(self, body, headers):
        url = f"{self.host}{self.notes_endpoint}"
        try:
            response = requests.post(url=url, json=body, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"call_create_note_api was failed: {e}")


    def call_delete_notes_api(self, note_id, headers):
        url = f"{self.host}{self.notes_endpoint}/{note_id}"
        try:
            response = requests.delete(url=url, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"call_create_note_api was failed: {e}")

    def call_get_notes_api(self, note_id, headers):
        url = f"{self.host}{self.notes_endpoint}/{note_id}"
        try:
            response = requests.get(url=url, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"call_get_notes_api was failed: {e}")

    @staticmethod
    def verify_note_title(expected_title, response_body):
        try:
            assert expected_title == response_body["data"]["title"]
            return 0

        except:
            logging.warning(f"\n---Actual({response_body["data"]["title"]}) title is not matching with expected({expected_title}) title")
            return 1

    @staticmethod
    def verify_note_description(expected_description, response_body):
        try:
            assert expected_description == response_body["data"]["description"]
            return 0

        except:
            logging.warning(f"\n---Actual({response_body["data"]["description"]}) description is not matching with expected({expected_description}) description")
            return 1


    @staticmethod
    def verify_note_category(expected_category, response_body):
        try:
            assert expected_category == response_body["data"]["category"]
            return 0

        except:
            logging.warning(f"\n---Actual({response_body["data"]["category"]}) category is not matching with expected({expected_category}) category")
            return 1