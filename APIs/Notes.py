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