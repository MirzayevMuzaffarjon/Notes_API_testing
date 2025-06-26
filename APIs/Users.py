import logging, requests
from APIs.Base_API import BaseAPI
import os
from dotenv import load_dotenv

class UsersAPI(BaseAPI):

    def call_user_register_api(self, body, headers):
        url = f"{self.host}{self.user_register_endpoint}"
        try:
            response = requests.post(url=url, json=body, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"---call_user_register_api was failed!!! Exception: {e}")