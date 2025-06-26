import logging, requests
from APIs.Base_API import BaseAPI


class UsersAPI(BaseAPI):

    def call_user_register_api(self, body, headers):
        url = f"{self.host}{self.user_register_endpoint}"
        try:
            response = requests.post(url=url, json=body, headers=headers)
            return response
        except Exception as e:
            logging.warning(f"---call_user_register_api was failed!!! Exception: {e}")

    def call_user_login_api(self, body, headers):
        url = f"{self.host}{self.user_login_endpoint}"
        try:
            response = requests.post(url=url, json=body, headers=headers)
            return response
        except Exception as e:
            logging.warning(f"---call_user_login_api was failed!!! Exception: {e}")