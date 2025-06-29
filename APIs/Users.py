import logging, requests
from APIs.Base_API import BaseAPI


class UsersAPI(BaseAPI):

    def call_user_register_api(self, body, headers):
        url = f"{self.host}{self.user_register_endpoint}"
        try:
            response = requests.post(url=url, json=body, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"\n---call_user_register_api was failed!!! Exception: {e}")


    def call_user_login_api(self, body, headers):
        url = f"{self.host}{self.user_login_endpoint}"
        try:
            response = requests.post(url=url, json=body, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"\n---call_user_login_api was failed!!! Exception: {e}")


    def call_user_delete_api(self, headers):
        url = f"{self.host}{self.user_delete_endpoint}"
        try:
            response = requests.delete(url=url, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"\n---call_user_delete_api was failed!!! Exception: {e}")


    def call_user_profile_api(self, headers):
        url = f"{self.host}{self.user_profile_endpoint}"
        try:
            response = requests.get(url=url, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"\n---call_user_profile_api was failed!!! Exception: {e}")


    def call_edit_profile_api(self, body, headers):
        url = f"{self.host}{self.user_edit_profile_endpoint}"
        try:
            response = requests.patch(url=url, json=body, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"\n---call_edit_profile_api was failed!!! Exception: {e}")


    def call_user_logout_api(self, headers):
        url = f"{self.host}{self.user_logout_endpoint}"
        try:
            response = requests.delete(url=url, headers=headers)
            return response

        except Exception as e:
            logging.warning(f"\n---call_user_logout_api was failed!!! Exception: {e}")


    @staticmethod
    def verify_name_is_correct(response_body, expected_name):
        try:
            assert response_body["data"]["name"] == expected_name
            return 0

        except:
            logging.warning(f"\n---Actual({response_body['data']['name']}) name isn't matching with expected({expected_name}) name")
            return 1


    @staticmethod
    def verify_email_is_correct(response_body, expected_email):
        try:
            assert response_body["data"]["email"] == expected_email
            return 0

        except:
            logging.warning(f"\n---Actual({response_body['data']['email']}) email isn't matching with expected({expected_email}) email")
            return 1


    @staticmethod
    def verify_phone_number_is_correct(response_body, expected_phone_number):
        try:
            assert response_body["data"]["phone"] == expected_phone_number
            return 0

        except:
            logging.warning(
                f"\n---Actual({response_body['data']['phone']}) phone isn't matching with expected({expected_phone_number}) phone")
            return 1


    @staticmethod
    def verify_company_name_is_correct(response_body, expected_company_name):
        try:
            assert response_body["data"]["company"] == expected_company_name
            return 0

        except:
            logging.warning(
                f"\n---Actual({response_body['data']['company']}) company isn't matching with expected({expected_company_name}) company")
            return 1